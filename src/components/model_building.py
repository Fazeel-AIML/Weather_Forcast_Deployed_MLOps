import pandas as pd
import joblib
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from loggings.logger import get_logger
from config.config import (
    PREPROCESSED_DATA_PATH,
    MODEL_PATH,
    METRICS_PATH,
    RANDOM_STATE,
    N_ESTIMATORS,
    TARGET_COLUMN
)

logger = get_logger(__name__)

class ModelTraining:
    def __init__(self):
        """Initialize model training configurations."""
        self.preprocessed_data_path = PREPROCESSED_DATA_PATH
        self.model_path = MODEL_PATH
        self.metrics_path = METRICS_PATH
        self.random_state = RANDOM_STATE
        self.n_estimators = N_ESTIMATORS
        self.target_column = TARGET_COLUMN

    def train(self):
        """Trains the model"""
        try:
            # Load preprocessed data
            df = pd.read_csv(self.preprocessed_data_path)
            X = df.drop(columns=[self.target_column])
            y = df[self.target_column]

            # Split data into training and testing sets
            x_train, x_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=self.random_state, stratify=y
            )

            # Initialize and train model
            model = RandomForestClassifier(n_estimators=self.n_estimators, random_state=self.random_state)
            model.fit(x_train, y_train)

            # Make predictions
            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)

            # Save model and metrics
            joblib.dump(model, self.model_path)
            with open(self.metrics_path, "w") as f:
                json.dump({"accuracy": accuracy, "classification_report": report}, f)

            logger.info(f"✅ Model trained and saved at {self.model_path}")
            logger.info(f"🎯 Accuracy: {accuracy:.4f}")

        except Exception as e:
            logger.error(f"❌ Error in model training: {e}")
            raise
