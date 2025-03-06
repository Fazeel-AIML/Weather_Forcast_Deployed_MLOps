import boto3
import os

# S3 Bucket Configuration
S3_BUCKET = "weatherfaze"
MODEL_FILE_NAME = "random_forest_model.pkl"
MODEL_LOCAL_PATH = "artifacts/random_forest_model.pkl"

# AWS Credentials from Environment Variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

# Initialize S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

# Download model from S3
def download_model():
    try:
        if not os.path.exists("artifacts"):
            os.makedirs("artifacts")
        s3.download_file(S3_BUCKET, MODEL_FILE_NAME, MODEL_LOCAL_PATH)
        print(f"✅ Model downloaded successfully: {MODEL_LOCAL_PATH}")
    except Exception as e:
        print(f"⚠️ Error downloading model: {e}")

if __name__ == "__main__":
    download_model()
