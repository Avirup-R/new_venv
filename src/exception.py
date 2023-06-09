import sys
import logging
from src.logger import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in script name [{0}] line number [{1}] error message [{2}]".fomat(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message
class CustomException(Exception):
    def _init_(self,error_message,error_details:sys):
        super()._init_(error_message) # inherit the error message
        self.error_message = error_message_details(error_message,error_details=error_details)

    def _str_(self):
        return self.error_message

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info('Zero Division error')
        raise CustomException(e,sys)