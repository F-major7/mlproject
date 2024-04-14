import sys #Contains info about exception
import logging

def error_message_detail(error, error_detail:sys): 
    '''
    Returns error message when hits an error
    '''
    _,_, exc_tb = error_detail.exc_info() # give info about which file and line is the eroor coming from
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    '''
    intorduce an error variable
    '''
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
    
