"""
Main workflow module for SpottyrWorkflow package.
"""

import json
import logging
import sys
import zipfile
import tempfile
import os
from pathlib import Path
from typing import Optional, Union, Dict, Any

try:
    from PIL import Image
except ImportError:
    raise ImportError("Pillow is required but not installed. Please install it with: pip install Pillow")

try:
    import onnxruntime as ort
except ImportError:
    raise ImportError("onnxruntime is required but not installed. Please install it with: pip install onnxruntime")


class WorkflowResult:
    """
    Container for workflow execution results.
    """

    def __init__(self, results_data: Dict[str, Any]):
        """Initialize with results data."""
        self._data = results_data

    @property
    def prediction(self) -> Any:
        """Get the prediction result from the workflow execution."""
        return self._data.get("prediction")

    @property
    def error(self) -> Optional[str]:
        """Get the error message if the workflow failed."""
        return self._data.get("error")

    @property
    def success(self) -> bool:
        """Check if the workflow execution was successful."""
        return self._data.get("error") is None

    def to_json(self) -> str:
        """Convert results to JSON string."""
        return json.dumps(self._data, indent=2)

    def to_dict(self) -> Dict[str, Any]:
        """Get the raw results data as a dictionary."""
        return self._data.copy()

    def __str__(self) -> str:
        """String representation of the workflow result."""
        if self.success:
            return str(self.prediction)
        else:
            return f"Error: {self.error}"

    def __repr__(self) -> str:
        """Detailed string representation of the workflow result."""
        return f"WorkflowResult({self._data})"


class SpottyrWorkflow:
    """
    A workflow management class with ZIP file handling capabilities.
    """

    def __init__(self, log_level: Union[int, str] = logging.ERROR):
        """
        Initialize the SpottyrWorkflow instance.

        Args:
            log_level: The logging level for the workflow. Can be an integer (logging.DEBUG,
                      logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL) or
                      a string ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
                      Default is logging.ERROR.
        """
        # Set up logging
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # Handle string log levels
        if isinstance(log_level, str):
            log_level = getattr(logging, log_level.upper(), logging.ERROR)

        self.logger.setLevel(log_level)

        # Create console handler if none exists
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

        self.loaded_path: Optional[Path] = None
        self.extracted_path: Optional[Path] = None
        self.models: Dict[str, ort.InferenceSession] = {}  # Multiple ONNX model sessions
        self.models_config: Dict[str, Dict[str, Any]] = {}  # Model configurations from JSON
        self.workflow_config: Optional[Dict[str, Any]] = None  # Overall workflow configuration

        self.logger.info("SpottyrWorkflow initialized with log level: %s", logging.getLevelName(log_level))

    def load(self, file_path: Union[str, Path], extract_to: Optional[Union[str, Path]] = None) -> Path:
        """
        Load and unzip a ZIP file if given a file path, or load directly from a directory.

        Args:
            file_path: Path to the ZIP file to load and extract, or path to a directory
            extract_to: Optional directory to extract to. If not provided,
                       extracts to a directory with the same name as the ZIP file

        Returns:
            Path: The path where the ZIP file was extracted or the directory path

        Raises:
            FileNotFoundError: If the ZIP file or directory doesn't exist
            zipfile.BadZipFile: If the file is not a valid ZIP file
        """
        file_path = Path(file_path)
        self.logger.debug(f"Attempting to load path: {file_path}")

        # Check if the file/directory exists
        if not file_path.exists():
            self.logger.error(f"Path not found: {file_path}")
            raise FileNotFoundError(f"Path not found: {file_path}")

        # If it's a directory, use it directly
        if file_path.is_dir():
            self.logger.info(f"Loading directory directly: {file_path}")
            self.loaded_path = file_path
            self.extracted_path = file_path
        else:
            # Check if it's a ZIP file
            if not zipfile.is_zipfile(file_path):
                self.logger.error(f"File is not a valid ZIP file: {file_path}")
                raise zipfile.BadZipFile(f"File is not a valid ZIP file: {file_path}")

            # Determine extraction directory
            if extract_to is None:
                extract_to = file_path.parent / file_path.stem
            else:
                extract_to = Path(extract_to)

            self.logger.info(f"Extracting ZIP file {file_path} to {extract_to}")

            # Create extraction directory if it doesn't exist
            extract_to.mkdir(parents=True, exist_ok=True)

            # Extract the ZIP file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)

            # Store the paths for reference
            self.loaded_path = file_path
            self.extracted_path = extract_to
            self.logger.debug(f"Successfully extracted ZIP file to: {extract_to}")

        # Automatically load ONNX model if signature.json is present
        config_path = self.extracted_path / "signature.json"
        if config_path.exists():
            self.logger.debug(f"Found signature.json, loading configuration: {config_path}")
            try:
                with open(config_path, 'r') as config_file:
                    config_data = json.load(config_file)
                    self.workflow_config = config_data  # Load the entire workflow config
                    self.models_config = config_data.get("models", {})

                    # Load each model defined in the configuration
                    for model_name, model_info in self.models_config.items():
                        model_path = model_info.get("path")
                        if model_path:
                            full_model_path = self.extracted_path / model_path
                            self.logger.debug(f"Loading model '{model_name}' from: {full_model_path}")
                            self.load_model(full_model_path, model_name)

                self.logger.info(f"Successfully loaded workflow configuration with {len(self.models)} models")
            except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
                # If config loading fails, continue without the model
                self.logger.warning(f"Could not load workflow config: {e}")
        else:
            self.logger.debug("No signature.json found, skipping automatic model loading")

        return self.extracted_path

    def invoke(self, image: Image.Image) -> WorkflowResult:
        """
        Execute the workflow by running main.py from the extracted package.

        Args:
            image: PIL Image object to process

        Returns:
            WorkflowResult: The result of the workflow execution

        Raises:
            RuntimeError: If no package has been loaded/extracted or no models are loaded
            FileNotFoundError: If main.py doesn't exist in the extracted package
        """
        self.logger.debug("Starting workflow execution")

        if self.extracted_path is None:
            self.logger.error("No package loaded. Call load() first to extract a workflow package.")
            raise RuntimeError("No package loaded. Call load() first to extract a workflow package.")

        if not self.models:
            self.logger.error("No ONNX models loaded. Models are required for workflow execution.")
            raise RuntimeError("No ONNX models loaded. Models are required for workflow execution.")

        # Check if main.py exists in the extracted directory
        main_py_path = self.extracted_path / "main.py"
        if not main_py_path.exists():
            self.logger.error(f"main.py not found in extracted package: {self.extracted_path}")
            raise FileNotFoundError(f"main.py not found in extracted package: {self.extracted_path}")

        self.logger.debug(f"Found main.py at: {main_py_path}")

        # Create a temporary file for the image
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_image:
            temp_image_path = temp_image.name

        self.logger.debug(f"Created temporary image file: {temp_image_path}")

        # Initialize result variable with a default error value
        result_to_return: WorkflowResult = WorkflowResult({"error": "Unknown error occurred"})

        try:
            # Save the PIL Image to the temporary file as JPEG (no alpha channel needed)
            # Convert to RGB if image has alpha channel to ensure JPEG compatibility
            if image.mode in ('RGBA', 'LA'):
                self.logger.debug(f"Converting image from {image.mode} to RGB")
                image = image.convert('RGB')
            image.save(temp_image_path, format='JPEG', quality=95)
            self.logger.debug("Image saved to temporary file")

            # Import the workflow's main module and set the pre-loaded model
            import importlib.util
            spec = importlib.util.spec_from_file_location("workflow_main", main_py_path)
            workflow_module = importlib.util.module_from_spec(spec)

            # Add the workflow directory to sys.path temporarily
            original_path = sys.path.copy()
            sys.path.insert(0, str(self.extracted_path))

            try:
                self.logger.debug("Loading workflow module")
                spec.loader.exec_module(workflow_module)

                # Check if the module has the set_preloaded_model function
                if hasattr(workflow_module, 'set_preloaded_model'):
                    self.logger.debug("Setting preloaded models in workflow module")
                    # Pass all pre-loaded models to the workflow
                    workflow_module.set_preloaded_model(self.models, self.models_config)

                # Execute the main function directly
                original_argv = sys.argv.copy()
                sys.argv = ['main.py', temp_image_path]

                # Capture stdout to get the result
                from io import StringIO
                import contextlib

                self.logger.debug("Executing workflow main function")
                stdout_capture = StringIO()
                with contextlib.redirect_stdout(stdout_capture):
                    workflow_module.main()

                # Restore original argv
                sys.argv = original_argv

                # Parse the captured output
                output = stdout_capture.getvalue().strip()
                if output:
                    self.logger.debug(f"Workflow output received: {output[:100]}...")  # Log first 100 chars
                    try:
                        output_data = json.loads(output)
                        result_to_return = WorkflowResult(output_data)
                        self.logger.info("Workflow execution completed successfully")
                    except json.JSONDecodeError as e:
                        error_msg = f"Failed to parse workflow output as JSON: {e}\nOutput: {output}"
                        self.logger.error(error_msg)
                        result_to_return = WorkflowResult({"error": error_msg})
                else:
                    error_msg = "No output from workflow"
                    self.logger.warning(error_msg)
                    result_to_return = WorkflowResult({"error": error_msg})

            finally:
                # Restore original sys.path
                sys.path = original_path

        except Exception as e:
            # Handle any unexpected exceptions during image saving or execution
            error_msg = f"Unexpected error during workflow execution: {str(e)}"
            self.logger.error(error_msg, exc_info=True)
            result_to_return = WorkflowResult({"error": error_msg})
        finally:
            # Clean up the temporary image file
            try:
                os.unlink(temp_image_path)
                self.logger.debug("Cleaned up temporary image file")
            except OSError:
                self.logger.warning("Failed to clean up temporary image file")

        return result_to_return

    def load_model(self, model_path: Union[str, Path], model_name: Optional[str] = None):
        """
        Load an ONNX model from the specified path.

        Args:
            model_path: Path to the ONNX model file
            model_name: Optional name to associate with the loaded model

        Raises:
            FileNotFoundError: If the model file doesn't exist
            RuntimeError: If there is an error loading the model
        """
        model_path = Path(model_path)
        self.logger.debug(f"Attempting to load ONNX model: {model_path}")

        # Check if the model file exists
        if not model_path.exists():
            self.logger.error(f"ONNX model file not found: {model_path}")
            raise FileNotFoundError(f"ONNX model file not found: {model_path}")

        # Load the ONNX model
        try:
            model_name = model_name or model_path.stem  # Use file stem as model name if not provided
            self.logger.debug(f"Loading ONNX model '{model_name}' from: {model_path}")
            self.models[model_name] = ort.InferenceSession(str(model_path))
            self.logger.info(f"Successfully loaded ONNX model: {model_name}")
        except Exception as e:
            self.logger.error(f"Error loading ONNX model '{model_name}': {e}")
            raise RuntimeError(f"Error loading ONNX model: {e}")

    def predict(self, input_data: Any, model_name: Optional[str] = None) -> Any:
        """
        Run inference on the input data using the loaded ONNX model.

        Args:
            input_data: The input data for the model
            model_name: Optional name of the model to use for prediction. If not provided,
                        the first loaded model will be used.

        Returns:
            The model's prediction

        Raises:
            RuntimeError: If no model is loaded or if there is an error during inference
        """
        self.logger.debug(f"Running prediction with model: {model_name or 'default'}")

        if not self.models:
            self.logger.error("No ONNX models loaded. Call load_model() first.")
            raise RuntimeError("No ONNX models loaded. Call load_model() first.")

        # Use the specified model or the first loaded model
        model = self.models.get(model_name) or next(iter(self.models.values()))
        actual_model_name = model_name or next(iter(self.models.keys()))
        self.logger.debug(f"Using model: {actual_model_name}")

        # Run inference
        try:
            ort_inputs = {model.get_inputs()[0].name: input_data}
            self.logger.debug("Running ONNX model inference")
            ort_outs = model.run(None, ort_inputs)
            self.logger.debug("ONNX model inference completed successfully")
            return ort_outs
        except Exception as e:
            self.logger.error(f"Error during ONNX model inference: {e}")
            raise RuntimeError(f"Error during ONNX model inference: {e}")
