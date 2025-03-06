# src/config/__init__.py

# Data Ingestion
RAW_DATA_PATH = "notebooks/weatherHistory.csv"
PREPROCESSED_DATA_PATH = "artifacts/preprocessed.csv"
TEST_SIZE = 0.2
RANDOM_STATE = 42

# Data Preprocessing
DROP_COLUMNS = ["Formatted Date", "Daily Summary", "Loud Cover"]
NUMERICAL_COLUMNS = [
    "Temperature (C)",
    "Apparent Temperature (C)",
    "Humidity",
    "Wind Speed (km/h)",
    "Wind Bearing (degrees)",
    "Visibility (km)",
    "Pressure (millibars)",
]
CATEGORICAL_COLUMNS = ["Summary", "Precip Type"]

# Model Configuration
MODEL_ALGORITHM = "RandomForestClassifier"
N_ESTIMATORS = 100
MAX_DEPTH = None  # No depth limit by default
MIN_SAMPLES_SPLIT = 2
MIN_SAMPLES_LEAF = 1
MODEL_RANDOM_STATE = 42
TARGET_COLUMN = "Precip Type"

# Training Configuration
BATCH_SIZE = 32
EPOCHS = 10
STRATIFY = True
VALIDATION_SPLIT = 0.1

# Artifacts Paths
MODEL_PATH = "artifacts/random_forest_model.pkl"
PREPROCESSED_DATA_PATH = "artifacts/preprocessed.csv"
METRICS_PATH = "artifacts/metrics.json"
ARCHIVE_PATH = "artifacts/archive"

# AWS S3 Configuration
AWS_ACCESS_KEY = "YOUR_AWS_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_AWS_SECRET_KEY"
AWS_REGION = "us-east-1"  # Change if using another region
S3_BUCKET = "weatherfaze"

# Paths Configuration
ARTIFACTS_DIR = "artifacts"
ARCHIVE_DIR = "artifacts/archive"

# CI/CD Configuration
DOCKER_IMAGE_NAME = "random_forest_classifier"
GITHUB_ACTIONS_ENABLED = True
DVC_TRACKING_ENABLED = True
AWS_S3_SYNC_ENABLED = True
