import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from loggings.logger import get_logger
from config.config import PREPROCESSED_DATA_PATH, DROP_COLUMNS, NUMERICAL_COLUMNS, CATEGORICAL_COLUMNS

logger = get_logger(__name__)

class DataPreprocessing:
    def __init__(self, df):
        """Initialize Data Preprocessing with the input DataFrame."""
        self.df = df
        self.preprocessed_data_path = PREPROCESSED_DATA_PATH

    def drop_columns(self):
        """Drops unnecessary columns"""
        try:
            self.df.drop(columns=DROP_COLUMNS, inplace=True)
            logger.info(f"Dropped columns: {DROP_COLUMNS}")
        except Exception as e:
            logger.error(f"Error dropping columns: {e}")
            raise

    def remove_outliers(self):
        """Removes outliers using IQR"""
        try:
            for col in NUMERICAL_COLUMNS:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                self.df = self.df[(self.df[col] >= (Q1 - 1.5 * IQR)) & (self.df[col] <= (Q3 + 1.5 * IQR))]
            logger.info("Outliers removed successfully")
        except Exception as e:
            logger.error(f"Error removing outliers: {e}")
            raise

    def encode_categorical(self):
        """Encodes categorical features using Label Encoding"""
        try:
            le = LabelEncoder()
            for col in CATEGORICAL_COLUMNS:
                self.df[col] = le.fit_transform(self.df[col])
            logger.info("Categorical encoding completed")
        except Exception as e:
            logger.error(f"Error encoding categorical variables: {e}")
            raise

    def save_preprocessed_data(self):
        """Saves preprocessed data"""
        try:
            self.df.to_csv(self.preprocessed_data_path, index=False)
            logger.info(f"✅ Preprocessed data saved at {self.preprocessed_data_path}")
        except Exception as e:
            logger.error(f"Error saving preprocessed data: {e}")
            raise

    def execute(self):
        """Runs the complete preprocessing pipeline"""
        try:
            self.drop_columns()
            self.remove_outliers()
            self.encode_categorical()
            self.save_preprocessed_data()
            logger.info("✅ Data preprocessing completed successfully!")
        except Exception as e:
            logger.error(f"❌ Data preprocessing failed: {e}")
            raise
