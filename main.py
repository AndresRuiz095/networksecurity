from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_transformation import DataTransformation


import sys



if __name__ == '__main__':
    try : 
        Trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(Trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("Initiate the data validatoin")
        data_validation_config = DataValidationConfig(Trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config) 
        logging.info('Initiate the data validation')
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info('data validation Complete')
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(Trainingpipelineconfig)
        data_Transformation = DataTransformation(data_validation_artifact ,data_transformation_config)
        data_transformation_artifact=data_Transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
        
    except Exception as e : 
        raise NetworkSecurityException(e,sys)
                     