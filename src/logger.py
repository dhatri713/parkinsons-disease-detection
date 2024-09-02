import logging
import os
from datetime import datetime

# Create a log directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "LOGS")
os.makedirs(log_dir, exist_ok=True)

# Generate a log file name with timestamp
log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Log level
    filename=log_file,   # Log file
    filemode='w',        # Write mode (overwrite each time)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log message format
)

# Example usage
if __name__ == "__main__":
    logging.info("Logging has started 2.0")
