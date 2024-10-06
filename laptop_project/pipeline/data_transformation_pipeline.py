import sys
from laptop_project.exception import LaptopException
from laptop_project.logger import logging

from laptop_project.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from laptop_project.pipeline.data_validation_pipeline import DataValidationPipeline

from laptop_project.components.data_validation import DataValidation
from laptop_project.components.data_transformation import DataTransformation


from laptop_project.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig,
                                                DataTransformationConfig)

from laptop_project.entity.artifact_entity import (DataIngestionArtifact,
                                                DataValidationArtifact,
                                                DataTransformationArtifact)



class DataTransformationPipeline:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
        
    def main(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_artifact: DataValidationArtifact) -> DataTransformationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data transformation component
        """
        try:
            data_transformation = DataTransformation(data_ingestion_artifact=data_ingestion_artifact,
                                                     data_transformation_config=self.data_transformation_config,
                                                     data_validation_artifact=data_validation_artifact)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
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
        
    except Exception as e:
        raise e