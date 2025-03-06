from components.data_ingestion import DataIngestion
from components.data_preprocessing import DataPreprocessing
from components.model_building import ModelTraining
from loggings.logger import get_logger

logger = get_logger(__name__)

def run_pipeline():
    try:
        logger.info("Starting ML Training Pipeline...")

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
    
    except Exception as e:
        logger.error(f"❌ Error in training pipeline: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()
