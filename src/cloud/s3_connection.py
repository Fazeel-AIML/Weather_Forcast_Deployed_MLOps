import boto3
import os
from loggings.logger import get_logger
from config.config import (
    AWS_REGION,
    S3_BUCKET,
    ARTIFACTS_DIR
)

# Fetch credentials from environment variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

logger = get_logger(__name__)

class S3Connector:
    def __init__(self):
        """Initialize S3 connection using credentials from config constants."""
        if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
            logger.error("❌ AWS credentials not found in environment variables.")
            raise ValueError("AWS credentials not set.")

        logger.info(f"🔄 Initializing S3 Connector for bucket: {S3_BUCKET}")

        self.s3_bucket = S3_BUCKET
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION,
        )

        self.artifact_path = ARTIFACTS_DIR
        
        # Ensure artifact directory exists
        os.makedirs(self.artifact_path, exist_ok=True)

    def upload_latest_artifacts(self):
        """Upload the latest artifacts to the S3 bucket."""
        try:
            if not os.path.exists(self.artifact_path):
                logger.error(f"❌ Artifacts directory {self.artifact_path} does not exist.")
                raise FileNotFoundError(f"Artifacts directory {self.artifact_path} not found.")

            for file_name in os.listdir(self.artifact_path):
                file_path = os.path.join(self.artifact_path, file_name)

                if os.path.isfile(file_path):
                    s3_key = f"artifacts/{file_name}"
                    self.s3_client.upload_file(file_path, self.s3_bucket, s3_key)
                    logger.info(f"✅ Uploaded {file_name} to S3 bucket {self.s3_bucket}")

        except Exception as e:
            logger.error(f"❌ Error uploading artifacts to S3: {e}")
            raise

if __name__ == "__main__":
    s3_connector = S3Connector()
    s3_connector.upload_latest_artifacts()
