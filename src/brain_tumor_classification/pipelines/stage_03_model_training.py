import sys
from brain_tumor_classification.utils.logger import logger
from brain_tumor_classification.utils.exception import CustomException
from brain_tumor_classification.config.configuration import ConfigurationManager
from brain_tumor_classification.components.prepare_callbacks import PrepareCallback
from brain_tumor_classification.components.stage_03_model_training import ModelTraining

class ModelTrainingPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            get_callbacks_config = config.get_prepare_callback_config()
            prepare_callbacks = PrepareCallback(config = get_callbacks_config)
            callbacks_list =  prepare_callbacks.create_TB_CP()
            logger.info('Callbacks Created Successfully...')

            training_config = config.get_model_training_config()
            model_training = ModelTraining(config = training_config)
            model_training.get_base_model()
            model_training.train_valid_generator()
            model_training.train_model(callbacks_list = callbacks_list)
        except Exception as e:
            raise CustomException(e,sys)



STAGE_NAME = "Model Training"

if  __name__ == "__main__":
    try:    
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info('-'*70)
    except Exception as e:
        raise CustomException(e,sys)