import sys
from typing import Tuple

import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from laptop_project.constants import PARAMS_FILE_PATH
from laptop_project.exception import LaptopException
from laptop_project.logger import logging
from laptop_project.utils.main_utils import load_numpy_array_data, read_yaml_file, load_object, save_object
from laptop_project.entity.config_entity import ModelTrainerConfig
from laptop_project.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact, RegressionMetricArtifact
from laptop_project.entity.estimator import LaptopModel

from catboost import CatBoostRegressor

class ModelTrainer:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact,
                 model_trainer_config: ModelTrainerConfig):
        """
        Args:
        data_transformation_artifact : DataTransformationArtifact object containing the preprocessed data
        model_trainer_config         : ModelTrainerConfig object containing the model trainer configuration parameters
        """
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config
        self._param_config = read_yaml_file(file_path=PARAMS_FILE_PATH)

    def get_model_object_and_report(self, train: np.array, test: np.array) -> Tuple[object, object]:
        """
        Method Name :   get_model_object_and_report
        Description :   This function uses neuro_mf to get the best model object and report of the best model
        
        Output      :   Returns metric artifact object and best model object
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            
            x_train, y_train, x_test, y_test = train[:, :-1], train[:, -1], test[:, :-1], test[:, -1]

            model_obj = CatBoostRegressor(iterations=self._param_config['ITERATIONS'], 
                                        learning_rate=self._param_config['LEARNING_RATE'],
                                        depth=self._param_config['DEPTH'], 
                                        random_seed=self._param_config['RANDOM_SEED'], verbose=False)
            
            model_obj.fit(x_train, y_train)  # Train the model on the training data
    
            # y_pred = model_obj.predict(x_test)
            
            # r2 = r2_score(y_test, y_pred) 
            # mse = mean_squared_error(y_test, y_pred)  
            # mae = mean_absolute_error(y_test, y_pred)  
            # metric_artifact = RegressionMetricArtifact(r2_score=r2, mae_score=mae, mse_score=mse)
            
            # return model_obj, metric_artifact
            return model_obj
        
        except Exception as e:
            raise LaptopException(e, sys) from e
        

    def initiate_model_trainer(self, ) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        """
        Method Name :   initiate_model_trainer
        Description :   This function initiates a model trainer steps
        
        Output      :   Returns model trainer artifact
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            train_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_file_path)
            test_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_file_path)
            
            # model_object ,metric_artifact = self.get_model_object_and_report(train=train_arr, test=test_arr)
            model_object = self.get_model_object_and_report(train=train_arr, test=test_arr)
            
            preprocessing_obj = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)

            laptop_model = LaptopModel(preprocessing_object = preprocessing_obj,
                                       trained_model_object = model_object)
            logging.info("Created laptop model object with preprocessor and model")
          
            save_object(self.model_trainer_config.trained_model_file_path, laptop_model)

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                # metric_artifact=metric_artifact,
            )
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise LaptopException(e, sys) from e