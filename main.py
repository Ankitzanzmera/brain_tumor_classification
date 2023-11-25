import sys
from brain_tumor_classification.utils.logger import logger
from brain_tumor_classification.utils.exception import CustomException

try:
    a = 1/0
    logger.info('Execution has started')
except Exception as e:
    raise CustomException(e,sys)


