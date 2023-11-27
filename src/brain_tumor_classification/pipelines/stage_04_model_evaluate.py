import sys
from brain_tumor_classification.utils.logger import logger
from brain_tumor_classification.utils.exception import CustomException
from brain_tumor_classification.config.configuration import ConfigurationManager
from brain_tumor_classification.components.stage_04_model_evaluate import ModelEvaluate

class ModelEvaluatePipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluate_config = config.get_model_evaluate_config()
            model_evaluate = ModelEvaluate(config=model_evaluate_config)
            model_evaluate.evaluate()
            model_evaluate.save_score()
        except Exception as e:
            raise e
        

STAGE_NAME = "Model Training"

if  __name__ == "__main__":
    try:    
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelEvaluatePipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info('-'*70)
    except Exception as e:
        raise CustomException(e,sys)