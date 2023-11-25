from brain_tumor_classification.constants import *
from brain_tumor_classification.utils.logger import logger
from brain_tumor_classification.utils.common import create_directories,read_yaml
from brain_tumor_classification.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILEPATH,params_filepath = PARAMS_FILEPATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        temp_config = self.config.data_ingestion

        create_directories([temp_config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = temp_config.root_dir,
            source = temp_config.source,
            local_data_file = temp_config.local_data_file,
            unzip_dir = temp_config.unzip_dir 
        )
        logger.info('Stored Data ingestion config')

        return data_ingestion_config
        
