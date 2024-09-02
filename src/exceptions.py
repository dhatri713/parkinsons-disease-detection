import sys
import os

# Adjust sys.path to include 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logger import logging  # Import logger

def generate_error_message(error_msg):
    _, _, exc_tb = sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    function_name = exc_tb.tb_frame.f_code.co_name
    message = "Error information:\nFilename: [{0}]\nFunction name: [{1}]\nLine number: [{2}]\nError: [{3}]".format(
        filename, function_name, lineno, error_msg)
    
    return message

class CustomException(Exception):
    def __init__(self, error_msg):
        self.error_msg = generate_error_message(error_msg)
        super().__init__(self.error_msg)
    
    def __str__(self):
        return self.error_msg

# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         # Log the exception
#         logging.error("An error occurred: %s", e)
#         # Raise a custom exception
#         raise CustomException(e)
