from brain_tumor_classification.constants import *
from brain_tumor_classification.utils.logger import logger
from brain_tumor_classification.utils.common import create_directories,read_yaml
from brain_tumor_classification.entity.config_entity import (DataIngestionConfig,
                                                            PrepareBaseModelConfig)

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
    
    def get_prepare_base_model_config(self):
        temp_config = self.config.prepare_base_model

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir= Path(temp_config.root_dir),
            base_model_path= Path(temp_config.base_model_path),
            updated_base_model_path= Path(temp_config.updated_base_model_path),
            params_image_size= self.params.IMAGE_SIZE,
            params_weights= self.params.WEIGHTS,
            params_include_top= self.params.INCLUDE_TOP,
            params_classes= self.params.CLASSES,
            params_learning_rate=self.params.LEARNING_RATE,
        )
        logger.info('Storing Prepare Base model Completed')
        return prepare_base_model_config
