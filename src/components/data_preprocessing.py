import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from config.config import config
from loggings.logger import get_logger

logger = get_logger(__name__)

class DataPreprocessing:
    def __init__(self, df):
        self.df = df
        self.preprocessed_data_path = config.get("data_ingestion")["preprocessed_data_path"]

    def drop_columns(self):
        """Drops unnecessary columns"""
        try:
            columns_to_drop = config.get("data_preprocessing")["drop_columns"]
            self.df.drop(columns=columns_to_drop, inplace=True)
            logger.info(f"Dropped columns: {columns_to_drop}")
        except Exception as e:
            logger.error(f"Error dropping columns: {e}")
            raise

    def remove_outliers(self):
        """Removes outliers using IQR"""
        try:
            columns = config.get("data_preprocessing")["numerical_columns"]
            for col in columns:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                self.df = self.df[(self.df[col] >= (Q1 - 1.5 * IQR)) & (self.df[col] <= (Q3 + 1.5 * IQR))]
            logger.info("Outliers removed")
        except Exception as e:
            logger.error(f"Error removing outliers: {e}")
            raise

    def encode_categorical(self):
        """Encodes categorical features"""
        try:
            categorical_cols = config.get("data_preprocessing")["categorical_columns"]
            le = LabelEncoder()
            for col in categorical_cols:
                self.df[col] = le.fit_transform(self.df[col])
            logger.info("Categorical encoding completed")
        except Exception as e:
            logger.error(f"Error encoding categorical variables: {e}")
            raise

    def save_preprocessed_data(self):
        """Saves preprocessed data"""
        self.df.to_csv(self.preprocessed_data_path, index=False)
        logger.info(f"Preprocessed data saved at {self.preprocessed_data_path}")

    def execute(self):
        """Runs the preprocessing pipeline"""
        self.drop_columns()
        self.remove_outliers()
        self.encode_categorical()
        self.save_preprocessed_data()
