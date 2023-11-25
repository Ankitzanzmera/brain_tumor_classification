import os,sys
from brain_tumor_classification.config.configuration import ConfigurationManager
from brain_tumor_classification.components.stage_01_data_ingestion import DataIngestion
from brain_tumor_classification.utils.exception import CustomException
from brain_tumor_classification.utils.logger import logger

class DataIngestionPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_file()   
        except Exception as e:
            raise CustomException(e,sys)
    
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
    

