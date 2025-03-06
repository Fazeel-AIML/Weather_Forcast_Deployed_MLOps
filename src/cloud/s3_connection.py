import boto3
import os
from config.config import config

class S3Connector:
    def __init__(self):
        """Initialize S3 connection using credentials from configuration.yaml."""
        aws_config = config.get("aws")
        self.s3_bucket = aws_config["s3_bucket"]
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_config["access_key"],
            aws_secret_access_key=aws_config["secret_key"],
            region_name=aws_config["region"],
        )

        self.artifact_path = config.get("paths")["artifacts"]
        
        # Ensure artifact directory exists
        os.makedirs(self.artifact_path, exist_ok=True)

    def upload_latest_artifacts(self):
        """Upload the latest artifacts to the S3 bucket."""
        for file_name in os.listdir(self.artifact_path):
            file_path = os.path.join(self.artifact_path, file_name)
            
            if os.path.isfile(file_path):
                s3_key = f"artifacts/{file_name}"
                self.s3_client.upload_file(file_path, self.s3_bucket, s3_key)
                print(f"✅ Uploaded {file_name} to S3 bucket {self.s3_bucket}")

if __name__ == "__main__":
    s3_connector = S3Connector()
    
    # Upload only the latest artifacts
    s3_connector.upload_latest_artifacts()
