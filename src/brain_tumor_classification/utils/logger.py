from datetime import datetime
import logging
import os,sys

dir_name = f"{datetime.now().strftime('%d_%m_%y')}"
DIR_PATH = os.path.join('logs',dir_name)
os.makedirs(DIR_PATH,exist_ok = True)

log_filename = f"{datetime.now().strftime('%H_%M_%S')}.log"
LOG_FILEPATH = os.path.join(DIR_PATH,log_filename)

logging.basicConfig(
    # filename= LOG_FILEPATH,
    format= "[ %(asctime)s ] - %(lineno)d - %(module)s - %(message)s",
    level= logging.INFO,
    handlers= [
        logging.FileHandler(LOG_FILEPATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("brain_tumor_classification")