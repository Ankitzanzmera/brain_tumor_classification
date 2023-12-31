import sys
from brain_tumor_classification.utils.logger import logger
from brain_tumor_classification.utils.exception import CustomException
from brain_tumor_classification.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from brain_tumor_classification.pipelines.stage_02_prepare_base_model import PrepareBaseModelPipeline
from brain_tumor_classification.pipelines.stage_03_model_training import ModelTrainingPipeline
from brain_tumor_classification.pipelines.stage_04_model_evaluate import ModelEvaluatePipeline

STAGE_NAME = "Data Ingestion"
if  __name__ == "__main__":
    try:    
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info('-'*70)
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
    

STAGE_NAME = "Model Evaluate"
if  __name__ == "__main__":
    try:    
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelEvaluatePipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info('-'*70)
    except Exception as e:
        raise CustomException(e,sys)