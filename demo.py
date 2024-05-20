from us_visa.logger import logging
from us_visa.exception import USvisaException
# logging.info("Welcome to Logging")
import sys
try:
    a= 1/"10"
    
except Exception as e:
    raise USvisaException(e, sys) from e
