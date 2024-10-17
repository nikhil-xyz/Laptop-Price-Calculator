from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    """
    Contains file paths for training and testing datasets.
    """
    trained_file_path:str 
    test_file_path:str 


@dataclass
class DataValidationArtifact:
    """
    Contains validation status, message, and drift report file path.
    """
    validation_status:bool
    message: str
    drift_report_file_path: str


@dataclass
class DataTransformationArtifact:
    """
    Contains file paths for transformed object and transformed datasets.
    """
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str


@dataclass
class RegressionMetricArtifact:
    """
    Contains regression metric scores.
    """
    r2_score:float
    mse_score:float
    mae_score:float


@dataclass
class ModelTrainerArtifact:
    """
    Contains file paths for trained model.
    """
    trained_model_file_path:str 


@dataclass
class ModelEvaluationArtifact:
    """
    Contains file paths for trained model.
    """
    trained_model_path:str


@dataclass
class ModelPusherArtifact:
    """
    Contains file paths for pushed model and s3 bucket name.
    """
    bucket_name:str
    s3_model_path:str