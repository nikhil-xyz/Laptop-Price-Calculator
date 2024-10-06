import sys
from laptop_project.exception import LaptopException
from laptop_project.logger import logging

from laptop_project.pipeline.data_ingestion_pipeline import DataIngestionPipeline

from laptop_project.components.data_validation import DataValidation


from laptop_project.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig)

from laptop_project.entity.artifact_entity import (DataIngestionArtifact,
                                                DataValidationArtifact)



class DataValidationPipeline:
    def __init__(self):
        self.data_validation_config = DataValidationConfig()
    
        
    def main(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config
                                             )

            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Performed the data validation operation")
            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )
            return data_validation_artifact
        except Exception as e:
            raise LaptopException(e, sys) from e



#   For DVC Pipeline
if __name__ == '__main__':
    try:

        # Instantiate the pipeline components and pass the necessary configurations and artifacts
        ingestion = DataIngestionPipeline()
        data_ingestion_artifact = ingestion.main()

        obj = DataValidationPipeline()
        data_validation_artifact = obj.main(data_ingestion_artifact = data_ingestion_artifact)
        
    except Exception as e:
        raise e