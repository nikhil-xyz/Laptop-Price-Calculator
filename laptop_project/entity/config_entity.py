import os
from laptop_project.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP:str = datetime.now().strftime('%d-%m-%Y-%H-%M')

@dataclass
class TrainingPipelineConfig:
    """
    Configures the training pipeline.

    Attributes:
    pipeline_name (str) : Name of the training pipeline.
    artifact_dir (str)  : Directory to store the artifacts of the training pipeline.
    timestamp (str)     : Timestamp for the training pipeline. Will play role in the artifact naming.
    """
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    """
    Configures the data ingestion process.

    Attributes:
    data_ingestion_dir (str)        : Directory to store the ingested data.
    feature_store_file_path (str)   : Path to the feature store file containing the ingested data.
    training_file_path (str)        : Path to the training file containing the ingested data.
    test_file_path (str)            : Path to the test file containing the ingest data.
    train_test_split_ratio (float)  : Ratio of training data to test data.
    collection_name (str)           : Name of the MongoDB collection containing the ingested data.
    """
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME


@dataclass
class DataValidationConfig:
    """
    Configures the data validation process.
    
    Attributes:
    data_validation_dir (str)         : Directory to store the data validation artifacts.
    drift_report_file_path_yaml (str) : Path to the drift report file containing the validation results.
    drift_report_file_path_html (str) : Path to the drift report file in HTML format containing the validation results.
    """
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    drift_report_file_path_yaml: str = os.path.join(data_validation_dir, DATA_VALIDATION_DRIFT_REPORT_DIR,
                                               DATA_VALIDATION_DRIFT_REPORT_FILE_NAME_YAML)
    drift_report_file_path_html: str = os.path.join(data_validation_dir, DATA_VALIDATION_DRIFT_REPORT_DIR,
                                               DATA_VALIDATION_DRIFT_REPORT_FILE_NAME_HTML)
    