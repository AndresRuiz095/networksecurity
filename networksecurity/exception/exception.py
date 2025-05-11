import sys 
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message , error_details : sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return 'El error ocurrio en el programa python con el nombre [{0}] en el numero de linea [{1}] mensaje de error [{2}]'.format(
            self.file_name,self.lineno , str(self.error_message))
    
