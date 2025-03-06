import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import json
from config.config import config
from loggings.logger import get_logger

logger = get_logger(__name__)

class ModelTraining:
    def __init__(self):
        self.preprocessed_data_path = config.get("data_ingestion")["preprocessed_data_path"]
        self.model_path = config.get("artifacts")["model_path"]
        self.metrics_path = config.get("artifacts")["metrics_path"]
        self.random_state = config.get("model")["random_state"]
        self.n_estimators = config.get("model")["n_estimators"]
        self.target_column = config.get("model")["target_column"]

    def train(self):
        """Trains the model"""
        try:
            df = pd.read_csv(self.preprocessed_data_path)
            X = df.drop(columns=[self.target_column])
            y = df[self.target_column]

            x_train, x_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=self.random_state, stratify=y
            )

            model = RandomForestClassifier(n_estimators=self.n_estimators, random_state=self.random_state)
            model.fit(x_train, y_train)

            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)

            joblib.dump(model, self.model_path)

            with open(self.metrics_path, "w") as f:
                json.dump({"accuracy": accuracy, "classification_report": report}, f)

            logger.info(f"Model trained and saved at {self.model_path}")
            logger.info(f"Accuracy: {accuracy}")

        except Exception as e:
            logger.error(f"Error in model training: {e}")
            raise
