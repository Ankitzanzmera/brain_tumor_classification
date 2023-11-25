import sys
from brain_tumor_classification.utils.logger import logger
from brain_tumor_classification.utils.exception import CustomException
from brain_tumor_classification.pipelines.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"

if  __name__ == "__main__":
    try:    
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info('-'*70)
    except Exception as e:
        raise CustomException
