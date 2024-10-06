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
