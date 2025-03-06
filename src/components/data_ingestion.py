import os
import pandas as pd
from loggings.logger import get_logger

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, data_path=r"notebooks\weatherHistory.csv", output_dir="artifacts"):
        self.data_path = data_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def load_data(self):
        try:
            logger.info(f"Loading data from {self.data_path}")
            df = pd.read_csv(self.data_path)
            logger.info(f"Data loaded successfully! Shape: {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise

    def save_data(self, df, filename="ingested_data.csv"):
        try:
            output_path = os.path.join(self.output_dir, filename)
            df.to_csv(output_path, index=False)
            logger.info(f"Data saved to {output_path}")
        except Exception as e:
            logger.error(f"Error saving data: {e}")
            raise

    def execute(self):
        try:
            df = self.load_data()
            self.save_data(df)
            logger.info("Data ingestion completed successfully!")
        except Exception as e:
            logger.error(f"Data ingestion failed: {e}")
            raise


if __name__ == "__main__":
    ingestion = DataIngestion()
    ingestion.execute()
