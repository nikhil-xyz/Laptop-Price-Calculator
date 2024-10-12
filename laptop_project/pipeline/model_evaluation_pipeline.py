import sys
from laptop_project.exception import LaptopException
from laptop_project.logger import logging

from laptop_project.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from laptop_project.pipeline.data_validation_pipeline import DataValidationPipeline
from laptop_project.pipeline.data_transformation_pipeline import DataTransformationPipeline
from laptop_project.pipeline.model_trainer_pipeline import ModelTrainerPipeline


from laptop_project.components.data_validation import DataValidation
from laptop_project.components.data_transformation import DataTransformation
from laptop_project.components.model_trainer import ModelTrainer
from laptop_project.components.model_evaluation_mlflow import ModelEvaluation


from laptop_project.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig,
                                                DataTransformationConfig,
                                                ModelTrainerConfig,
                                                ModelEvaluationConfig)

from laptop_project.entity.artifact_entity import (DataIngestionArtifact,
                                                DataValidationArtifact,
                                                DataTransformationArtifact,
                                                 ModelTrainerArtifact)



class ModelEvaluationPipeline:
    def __init__(self):
        self.model_evaluation_config = ModelEvaluationConfig()

    def main(self, data_ingestion_artifact: DataIngestionArtifact,
                                model_trainer_artifact: ModelTrainerArtifact):
        """
        This method of TrainPipeline class is responsible for starting modle evaluation
        """
        try:
            model_evaluation = ModelEvaluation(model_eval_config=self.model_evaluation_config,
                                                data_ingestion_artifact=data_ingestion_artifact,
                                                model_trainer_artifact=model_trainer_artifact)
            model_evaluation_artifact = model_evaluation.initiate_model_evaluation()
            return model_evaluation_artifact
        except Exception as e:
            raise LaptopException(e, sys)



#   For DVC Pipeline
if __name__ == '__main__':
    try:

        # Instantiate the pipeline components and pass the necessary configurations and artifacts
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
        
    except Exception as e:
        raise e