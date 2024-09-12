import os
import sys
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, r2_score

from dataclasses import dataclass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object
from src.utils import evaluate_models

@dataclass
class ModelTrainerConfig():
    model_trainer_obj_filepath = os.path.join('data', 'model_trainer.pkl')

class ModelTrainer():
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_array, test_array):
        try:
            X_train, y_train, X_test, y_test = (
            train_array[:, :-1],
            train_array[:, -1],
            test_array[:, :-1],
            test_array[:, -1]
        )
            
            logging.info("target and input features separated")

            models = {
                "KNN": KNeighborsClassifier(n_neighbors=5),
                "SVC": SVC(),
                "XGB": XGBClassifier()
            }

            model_report: dict = evaluate_models(X_train, y_train, X_test, y_test, models)

            best_score_model = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_score_model)
            ]
            best_model = models[best_model_name]

            logging.info("best model chosen")

            save_object(
                filepath=self.model_trainer_config.model_trainer_obj_filepath,
                preprocess_obj=best_model
            )

            logging.info("model saved")

            y_pred = best_model.predict(X_test)
            r2 = r2_score(y_test, y_pred)

            return r2
        
        except Exception as e:
            raise CustomException(e)