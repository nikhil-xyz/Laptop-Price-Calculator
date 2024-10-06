import os
from datetime import date


# Database Constants
DATABASE_NAME = "Laptop"
COLLECTION_NAME = "laptop_data"
MONGODB_URI = "MONGODB_URI"

PIPELINE_NAME: str = "laptop"
ARTIFACT_DIR: str = "artifact"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

FILE_NAME: str = "laptop.csv"
MODEL_FILE_NAME = "model.pkl"


TARGET_COLUMN = "Price"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")



"""
Data Ingestion Constants
"""
DATA_INGESTION_COLLECTION_NAME:str = "laptop_data"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2


"""
Data Validation Constants
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME_YAML: str = "report.yaml"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME_HTML: str = "html_report.html"


"""
Data Transformation Constants
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"