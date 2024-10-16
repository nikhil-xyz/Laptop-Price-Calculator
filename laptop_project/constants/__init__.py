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
PARAMS_FILE_PATH = os.path.join("params.yaml")


AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "eu-north-1"


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


"""
Model Trainer Constants
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
# MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
# MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")


"""
Model Pusher constants 
"""
# MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "laptop-model2024"
MODEL_PUSHER_S3_KEY = "model-registry"

APP_HOST = "0.0.0.0"
APP_PORT = 8085
