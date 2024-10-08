import sys
import os
from logger import logging


def error_message_detail(error, error_detail: sys):
    """
    This function extracts and formats the error details, including the file name,
    line number, and error message.
    """
    # Gets the traceback object
    _, _, exc_tb = error_detail.exc_info()  
    # Retrieves the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom exception class that formats the error message using the error_message_detail function.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


'''
if __name__=="__main__":
    
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
'''

