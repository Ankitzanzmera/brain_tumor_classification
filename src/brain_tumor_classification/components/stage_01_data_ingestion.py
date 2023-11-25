import gdown
import os,sys
import zipfile
from pathlib import Path
from brain_tumor_classification.utils.logger import logger
from brain_tumor_classification.utils.common import get_size
from brain_tumor_classification.utils.exception import CustomException
from brain_tumor_classification.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            gdown.download(self.config.source,self.config.local_data_file,quiet=False)
            logger.info(f'{self.config.local_data_file} Downloaded')
        else:
            logger.info(f'File Already Exists: {get_size(Path(self.config.local_data_file))}')

    def extract_file(self):
        try:
            unzip_path = self.config.unzip_dir
            with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f'Zip File Extracted Successfully at {unzip_path}')
        except Exception as e:
            raise CustomException(e,sys)