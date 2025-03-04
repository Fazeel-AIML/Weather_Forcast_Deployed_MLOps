import os
import pathlib

# Define directory and file structure
dirs = [
    "logs",
    "logs/logging.py",
    "logs/exceptions.py",
    
    "src",
    "src/components",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_preprocessing.py",
    "src/components/model_building.py",
    "src/components/training.py",
    "src/components/evaluation.py",
    "src/components/predict.py",
    
    "src/cloud",
    "src/cloud/__init__.py",
    "src/cloud/s3_connection.py",
    
    "src/config",
    "src/config/__init__.py",
    "src/config/config.py",
    
    "config",
    "config/__init__.py",
    "config/configuration.yaml",
    
    "artifacts",  # Store trained models, preprocessed data, etc.
    
    "notebooks",  # Jupyter notebooks for experimentation
    
    "scripts",
    "scripts/__init__.py",  # For automation scripts
    "scripts/train_pipeline.py",
    "scripts/predict_pipeline.py",
    
    ".github/workflows",  # GitHub Actions for CI/CD
    
    "dvc.yaml",
    "Dockerfile",
    "requirements.txt",
    "README.md",
    ".gitignore",
    "setup.py",  # If making it a package
    "main.py"  # Main entry point for the app
]

# Create directories and files
for path in dirs:
    path = pathlib.Path(path)
    
    # Force treating certain filenames as files, even if they have no extension
    if path.name in {"Dockerfile", ".gitignore", "README.md", "dvc.yaml", "requirements.txt", "setup.py", "main.py"}:
        path.touch(exist_ok=True)
    elif path.suffix:  # If path has a file extension, create an empty file
        path.parent.mkdir(parents=True, exist_ok=True)  # Ensure parent directory exists
        path.touch(exist_ok=True)  # Create file
    else:  # Create directory
        path.mkdir(parents=True, exist_ok=True)

print("Project structure created successfully!")
