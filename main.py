from src.datascience_project import logger
from src.datascience_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience_project.pipeline.data_validation_pipleline import DataValidationTrainingPipeline
from src.datascience_project.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience_project.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.datascience_project.config.configuration import ConfigurationManager
from src.datascience_project.pipeline.model_trainer_pipleine import ModelTrainerPipeline
STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Trainer stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Evaluation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e