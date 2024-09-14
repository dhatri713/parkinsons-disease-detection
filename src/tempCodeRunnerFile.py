import os
import sys

import numpy as np
import pandas as pd

#import dill
import pickle

from src.exceptions import CustomException

def save_object(filepath, preprocess_obj):
    try:
        dir_path = os.path.dirname(filepath)

        os.makedirs(dir_path, exist_ok=True)

        with open(filepath, "wb") as file_obj:
            pickle.dump(preprocess_obj, file_obj)

    except Exception as e:
        raise CustomException(e)