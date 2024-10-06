import sys
from laptop_project.exception import LaptopException
from laptop_project.logger import logging

from laptop_project.components.data_ingestion import DataIngestion


from laptop_project.entity.config_entity import DataIngestionConfig
from laptop_project.entity.artifact_entity import DataIngestionArtifact


class DataIngestionPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    def main(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_ingestion method of DataIngestionPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise LaptopException(e, sys) from e


if __name__ == '__main__':
    try:
        obj = DataIngestionPipeline()
        data_ingestion_artifact = obj.main()
        
    except Exception as e:
        raise e