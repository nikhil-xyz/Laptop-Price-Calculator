
import sys
from laptop_project.logger import logging
from laptop_project.exception import LaptopException
from laptop_project.pipeline.data_ingestion_pipeline import DataIngestionPipeline 
from laptop_project.pipeline.data_validation_pipeline import DataValidationPipeline
from laptop_project.pipeline.data_transformation_pipeline import DataTransformationPipeline
from laptop_project.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from laptop_project.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from laptop_project.pipeline.model_pusher_pipeline import ModelPusherPipeline

def run_pipeline():
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            ingestion = DataIngestionPipeline()
            data_ingestion_artifact = ingestion.main()

            validation = DataValidationPipeline()
            data_validation_artifact = validation.main(data_ingestion_artifact = data_ingestion_artifact)

            transformation = DataTransformationPipeline()
            data_transformation_artifact = transformation.main(
                data_ingestion_artifact=data_ingestion_artifact, data_validation_artifact=data_validation_artifact)

            trainer = ModelTrainerPipeline()
            model_trainer_artifact = trainer.main(data_transformation_artifact=data_transformation_artifact)

            evaluation = ModelEvaluationPipeline()
            model_evaluation_artifact = evaluation.main(data_ingestion_artifact=data_ingestion_artifact,
                                                      model_trainer_artifact=model_trainer_artifact)

            pusher = ModelPusherPipeline()
            model_pusher_artifact = pusher.main(model_evaluation_artifact=model_evaluation_artifact)


        except Exception as e:
            raise LaptopException(e, sys)


run_pipeline()