# Spottyr Edge Runtime

A Python library for running Spottyr AI workflows on edge devices. This runtime allows you to package, deploy, and execute machine learning workflows with ONNX models in a standardized way.

## Features

- **Workflow Packaging**: Load and execute workflows from ZIP files or directories
- **ONNX Model Support**: Automatic loading and management of ONNX models
- **Structured Output**: JSON-based result handling with error management
- **Edge Device Optimized**: Lightweight runtime suitable for edge deployment
- **Flexible Configuration**: JSON-based workflow configuration with `signature.json`

## Installation

### From PyPI

```bash
pip install spottyr-edge-runtime
```

### Dependencies

The package requires Python 3.8+ and the following dependencies:
- Pillow >= 9.0.0
- numpy >= 1.22.0
- opencv-python >= 4.8.0.74
- onnxruntime >= 1.12.0

## Quick Start

### Basic Usage

```python
from spottyr_edge_runtime.workflow import SpottyrWorkflow
from PIL import Image

# Create workflow instance
workflow = SpottyrWorkflow()

# Load workflow from ZIP file
workflow.load("path/to/workflow.zip")

# Load an image
image = Image.open("path/to/image.jpg")

# Execute the workflow
result = workflow.invoke(image)

# Check results
if result.success:
    print(f"Prediction: {result.prediction}")
else:
    print(f"Error: {result.error}")
```

## Creating Your Own Workflow

To create a workflow that works with the Spottyr Edge Runtime:

1. Create a directory with your workflow files
2. Include a `signature.json` configuration file
3. Create a `main.py` entry point
4. Add your ONNX model files
5. Package as a ZIP file for distribution

## Workflow Structure

### Directory Layout

A workflow package should have the following structure:

```
workflow_package/
├── main.py              # Entry point script
├── signature.json       # Workflow configuration
├── model.onnx          # ONNX model file(s)
└── additional_modules.py # Supporting code
```

### signature.json Configuration

The `signature.json` file defines the workflow configuration:

```json
{
  "models": {
    "model_name": {
      "type": "onnx",
      "path": "model.onnx",
      "conf_threshold": 0.6,
      "iou_threshold": 0.5,
      "class_names": ["class1", "class2", "class3"]
    }
  },
  "workflow": {
    "name": "Workflow Name",
    "version": "1.0.0",
    "description": "Workflow description"
  },
  "classes": {
    "Label": ["label1", "label2", "label3"]
  }
}
```

### main.py Entry Point

Your workflow's `main.py` should:

1. Accept an image path as a command line argument
2. Process the image using the loaded ONNX model
3. Output results as JSON to stdout

```python
#!/usr/bin/env python3
import sys
import json

def set_preloaded_model(models, models_config=None):
    """Called by SpottyrWorkflow to provide pre-loaded models"""
    global PRELOADED_MODELS
    PRELOADED_MODELS = models

def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python main.py <image_path>"}))
        return
    
    image_path = sys.argv[1]

    # Process image with your model
    prediction = process_image(image_path)
    
    # Output result as JSON
    result = {
        "prediction": prediction,
        "success": True
    }
    print(json.dumps(result))

if __name__ == "__main__":
    main()
```

