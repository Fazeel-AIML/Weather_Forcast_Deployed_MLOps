import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Define log file name with timestamp
log_filename = os.path.join(LOGS_DIR, f"app_{datetime.now().strftime('%Y-%m-%d')}.log")

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(module)s | %(message)s",
    handlers=[
        logging.FileHandler(log_filename),  # Save logs to file
        logging.StreamHandler()  # Print logs to console
    ]
)

# Function to get a logger
def get_logger(name: str):
    return logging.getLogger(name)

# Example usage (Uncomment below lines to test)
# logger = get_logger(__name__)
# logger.info("This is an info message")
# logger.warning("This is a warning")
# logger.error("This is an error")
