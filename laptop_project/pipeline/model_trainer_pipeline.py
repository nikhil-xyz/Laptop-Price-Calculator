import sys
from laptop_project.exception import LaptopException
from laptop_project.logger import logging

from laptop_project.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from laptop_project.pipeline.data_validation_pipeline import DataValidationPipeline
from laptop_project.pipeline.data_transformation_pipeline import DataTransformationPipeline


from laptop_project.components.data_validation import DataValidation
from laptop_project.components.data_transformation import DataTransformation
from laptop_project.components.model_trainer import ModelTrainer


from laptop_project.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig,
                                                DataTransformationConfig,
                                                ModelTrainerConfig)

from laptop_project.entity.artifact_entity import (DataIngestionArtifact,
                                                DataValidationArtifact,
                                                DataTransformationArtifact,
                                                 ModelTrainerArtifact)



class ModelTrainerPipeline:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
        
    def main(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        """
        This method of TrainPipeline class is responsible for starting data transformation component
        """
        try:
            model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact,
                                            model_trainer_config=self.model_trainer_config
                                            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
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
        
    except Exception as e:
        raise e