import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.logger import logging
from src.exceptions import CustomException

@dataclass
class DataIngestionConfig:
    base_path: str=os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    
    # Create the 'data' folder at the same level as 'src'
    data_folder: str=os.path.join(base_path, 'data')
    train_data_path: str=os.path.join(data_folder, 'train.csv')
    test_data_path: str=os.path.join(data_folder, 'test.csv')
    raw_data_path: str=os.path.join(data_folder, 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self):
        try:
            # Log the start of data ingestion
            logging.info("Starting data ingestion")
            
            # Ensure the directory for train and test data exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # Read the raw data from CSV
            raw_data = pd.read_csv("notebook/parkinsons.data")
            logging.info("Raw data loaded")
            
            # Split the data into train and test datasets
            train_data, test_data = train_test_split(raw_data, test_size=0.2, random_state=42)
            logging.info("Train-test split completed")
            
            # Save the train and test datasets to the respective paths
            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            raw_data.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train and test data saved as CSV files")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            # Handle exceptions and raise a custom exception
            raise CustomException(e)


if __name__ == "__main__":
    ingestor = DataIngestion()
    train_data, test_data = ingestor.start_data_ingestion()
