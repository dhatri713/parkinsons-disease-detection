import os
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.logger import logging
from src.exceptions import CustomException
from src.utils import save_object

@dataclass
class DataTransformationConfig():
    preprocessor_obj_filepath = os.path.join('data',"proprocessor.pkl") # this is where the pickl file for the preprocessor will be stored

class DataTransformation():
    def __init__(self):
        self.preprocessor_obj_config = DataTransformationConfig()
    
    def get_data_transformer_obj(self):
        try:
            columns = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
       'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
       'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
       'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA',
       'spread1', 'spread2', 'D2', 'PPE']
            
            pipeline = Pipeline(
                steps=[
                    ("scaler", StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ("pipeline", pipeline, columns)
                ]
            )

            logging.info("Transformer made")

            return preprocessor
        except Exception as e:
            raise CustomException(e)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("Train and test data read")
            logging.info("Obtaining preprocessor object")

            X_train = train_data.drop(["status", "name"], axis=1)
            y_train = train_data["status"]
            X_test = test_data.drop(["status", "name"], axis=1)
            y_test = test_data["status"]

            preprocessing_obj = self.get_data_transformer_obj()

            X_train_arr = preprocessing_obj.fit_transform(X_train)
            X_test_arr = preprocessing_obj.transform(X_test)

            train_arr = np.c_[
                X_train_arr, np.array(y_train)
            ]

            test_arr = np.c_[
                X_test_arr, np.array(y_test)
            ]

            logging.info("Test and train data trasnformed")

            save_object(
                filepath=self.preprocessor_obj_config.preprocessor_obj_filepath,
                preprocess_obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.preprocessor_obj_config.preprocessor_obj_filepath
            )
        except Exception as e:
            raise CustomException(e)