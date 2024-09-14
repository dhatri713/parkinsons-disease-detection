import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.utils import load_object
from src.exceptions import CustomException
from src.logger import logging

class PredictPipeline():
   def __init__(self, features) -> None:
       self.features = features

   def predict(self):
        try:
            preprocessor_path = os.path.join("data", "proprocessor.pkl")
            model_path = os.path.join("data", "model_trainer.pkl")
            preprocessor_obj = load_object(preprocessor_path)
            model_trainer_obj = load_object(model_path)
            transformed_features = preprocessor_obj.transform(self.features)
            preds = model_trainer_obj.predict(transformed_features)
            return preds
        except Exception as e:
            raise CustomException(e)


class CustomData():
    def __init__(self,
                MDVP_Fo_Hz: float,
                MDVP_Fhi_Hz: float,
                MDVP_Flo_Hz: float,
                MDVP_Jitter_Percent: float,
                MDVP_Jitter_Abs: float,
                MDVP_RAP: float,
                MDVP_PPQ: float,
                Jitter_DDP: float,
                MDVP_Shimmer: float,
                MDVP_Shimmer_dB: float,
                Shimmer_APQ3: float,
                Shimmer_APQ5: float,
                MDVP_APQ: float,
                Shimmer_DDA: float,
                NHR: float,
                HNR: float,
                RPDE: float,
                DFA: float,
                spread1: float,
                spread2: float,
                D2: float,
                PPE: float
                ):
        
        self.MDVP_Fo_Hz = MDVP_Fo_Hz
        self.MDVP_Fhi_Hz = MDVP_Fhi_Hz
        self.MDVP_Flo_Hz = MDVP_Flo_Hz
        self.MDVP_Jitter_Percent = MDVP_Jitter_Percent
        self.MDVP_Jitter_Abs = MDVP_Jitter_Abs
        self.MDVP_RAP = MDVP_RAP
        self.MDVP_PPQ = MDVP_PPQ
        self.Jitter_DDP = Jitter_DDP
        self.MDVP_Shimmer = MDVP_Shimmer
        self.MDVP_Shimmer_dB = MDVP_Shimmer_dB
        self.Shimmer_APQ3 = Shimmer_APQ3
        self.Shimmer_APQ5 = Shimmer_APQ5
        self.MDVP_APQ = MDVP_APQ
        self.Shimmer_DDA = Shimmer_DDA
        self.NHR = NHR
        self.HNR = HNR
        self.RPDE = RPDE
        self.DFA = DFA
        self.spread1 = spread1
        self.spread2 = spread2
        self.D2 = D2
        self.PPE = PPE

    def convert_ip_to_df(self):
        try:
            ip_dict = {
                "MDVP_Fo_Hz": [self.MDVP_Fo_Hz],
                "MDVP_Fhi_Hz": [self.MDVP_Fhi_Hz],
                "MDVP_Flo_Hz": [self.MDVP_Flo_Hz],
                "MDVP_Jitter_Percent": [self.MDVP_Jitter_Percent],
                "MDVP_Jitter_Abs": [self.MDVP_Jitter_Abs],
                "MDVP_RAP": [self.MDVP_RAP],
                "MDVP_PPQ": [self.MDVP_PPQ],
                "Jitter_DDP": [self.Jitter_DDP],
                "MDVP_Shimmer": [self.MDVP_Shimmer],
                "MDVP_Shimmer_dB": [self.MDVP_Shimmer_dB],
                "Shimmer_APQ3": [self.Shimmer_APQ3],
                "Shimmer_APQ5": [self.Shimmer_APQ5],
                "MDVP_APQ": [self.MDVP_APQ],
                "Shimmer_DDA": [self.Shimmer_DDA],
                "NHR": [self.NHR],
                "HNR": [self.HNR],
                "RPDE": [self.RPDE],
                "DFA": [self.DFA],
                "spread1": [self.spread1],
                "spread2": [self.spread2],
                "D2": [self.D2],
                "PPE": [self.PPE]
            }
            
            input_df = pd.DataFrame(ip_dict)
            return input_df

        except Exception as e:
            raise CustomException(e)
        

if __name__ == "__main__":
    try:
        data = CustomData(
            MDVP_Fo_Hz=120.552,
            MDVP_Fhi_Hz=131.162,
            MDVP_Flo_Hz=113.787,
            MDVP_Jitter_Percent=0.00968,
            MDVP_Jitter_Abs=0.00008,
            MDVP_RAP=0.00463,
            MDVP_PPQ=0.0075,
            Jitter_DDP=0.01388,
            MDVP_Shimmer=0.04701,
            MDVP_Shimmer_dB=0.456,
            Shimmer_APQ3=0.02328,
            Shimmer_APQ5=0.03526,
            MDVP_APQ=0.03243,
            Shimmer_DDA=0.06985,
            NHR=0.01222,
            HNR=21.378,
            RPDE=0.415564,
            DFA=0.825069,
            spread1=-4.242867,
            spread2=0.299111,
            D2=2.18756,
            PPE=0.357775
        )
    
        pred_df = data.convert_ip_to_df()
        predict_pipeline = PredictPipeline(pred_df)
        result = predict_pipeline.predict()
        if result[0] == 0.:
            res = "Absent"
        else:
            res = "Present"
        print(res)
        print(pred_df.head())
    except Exception as e:
        raise CustomException(e)