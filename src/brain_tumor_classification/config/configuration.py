import os
from pathlib import Path
from brain_tumor_classification.constants import *
from brain_tumor_classification.utils.logger import logger
from brain_tumor_classification.utils.common import create_directories,read_yaml
from brain_tumor_classification.entity.config_entity import (DataIngestionConfig,
                                                            PrepareBaseModelConfig,
                                                            PrepareCallbackConfig,
                                                            ModelTrainingConfig,
                                                            ModelEvaluateConfig)

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
    
    def get_prepare_callback_config(self) -> PrepareCallbackConfig:
        temp_config = self.config.prepare_callbacks

        create_directories([temp_config.root_dir])

        prepare_callback_config = PrepareCallbackConfig(
            root_dir = temp_config.root_dir,
            tensorboard_log_dir = temp_config.tensorboard_log_dir,
            checkpoint_model_path = temp_config.checkpoint_model_path
        )

        return prepare_callback_config
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        temp_config = self.config.model_training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data_path = os.path.join(self.config.data_ingestion.unzip_dir,"brain_tumor_mris","Training")
        validation_data_path = os.path.join(self.config.data_ingestion.unzip_dir,"brain_tumor_mris","Validation")

        create_directories([temp_config.root_dir])
        
        model_training_config = ModelTrainingConfig(
            root_dir= Path(temp_config.root_dir),
            trained_model_path= Path(temp_config.trained_model_path),
            updated_base_model= Path(prepare_base_model.updated_base_model_path),
            training_data = Path(training_data_path),
            validation_data= Path(validation_data_path),
            params_is_augmentation= params.AUGMENTATION,
            params_image_size= params.IMAGE_SIZE,
            params_batch_size= params.BATCH_SIZE,
            params_epochs= params.EPOCHS        
        )
        return model_training_config
    
    def get_model_evaluate_config(self) -> ModelEvaluateConfig:

        test_data_path = os.path.join(self.config.data_ingestion.unzip_dir,"brain_tumor_mris","Testing")
        model_evaluate_config = ModelEvaluateConfig(
            path_of_model= Path(self.config.model_training.trained_model_path),
            test_data_path= Path(test_data_path),
            params_batch_size= self.params.BATCH_SIZE,
            params_image_size= self.params.IMAGE_SIZE
        )
        return model_evaluate_config
