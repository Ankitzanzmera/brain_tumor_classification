import sys
from brain_tumor_classification.config.configuration import ConfigurationManager
from brain_tumor_classification.components.stage_02_prepare_base_model import PrepareBaseModel
from brain_tumor_classification.utils.exception import CustomException
from brain_tumor_classification.utils.logger import logger

class PrepareBaseModelPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise CustomException(e,sys)
        


STAGE_NAME = "Prepare Base Model"

if  __name__ == "__main__":
    try:    
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info('-'*70)
    except Exception as e:
        raise CustomException(e,sys)