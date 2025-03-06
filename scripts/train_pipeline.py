from components.data_ingestion import DataIngestion
from components.data_preprocessing import DataPreprocessing
from components.model_building import ModelTraining
from cloud.s3_connection import S3Connector
from loggings.logger import get_logger
import os

logger = get_logger(__name__)

def run_pipeline():
    try:
        logger.info("Starting ML Training Pipeline...")

        # Debugging AWS Credentials
        aws_key = os.getenv("AWS_ACCESS_KEY")
        aws_secret = os.getenv("AWS_SECRET_KEY")

        if not aws_key or not aws_secret:
            logger.error("❌ AWS credentials are missing in environment variables.")
            raise ValueError("AWS credentials are not set.")

        # 1️⃣ Data Ingestion
        data_ingestion = DataIngestion()
        df = data_ingestion.load_data()

        # 2️⃣ Data Preprocessing
        data_preprocessing = DataPreprocessing(df)
        data_preprocessing.execute()

        # 3️⃣ Model Training
        model_training = ModelTraining()
        model_training.train()

        logger.info("✅ ML Training Pipeline Completed Successfully!")
        
        # 4️⃣ Upload Artifacts to S3
        s3_connector = S3Connector()
        s3_connector.upload_latest_artifacts()
        logger.info("✅ Successfully Uploaded to S3")
        
    except Exception as e:
        logger.error(f"❌ Error in training pipeline: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()
