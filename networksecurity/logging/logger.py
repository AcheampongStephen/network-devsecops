import logging
import os
from datetime import datetime

# Define the log directory at the root of the project
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))  # Navigate to root
LOG_DIR = os.path.join(ROOT_DIR, "logs")  # Set logs directory in root
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure logs directory exists

# Generate log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)  # Full path for log file

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Test logging
logging.info("Logging system initialized successfully!")
print(f"Logs are being saved in: {LOG_FILE_PATH}")
