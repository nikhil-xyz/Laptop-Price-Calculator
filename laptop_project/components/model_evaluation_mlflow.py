import mlflow
from laptop_project.entity.config_entity import ModelEvaluationConfig
from laptop_project.entity.artifact_entity import ModelTrainerArtifact, DataIngestionArtifact, RegressionMetricArtifact,\
                                    ModelEvaluationArtifact
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from laptop_project.exception import LaptopException
from laptop_project.constants import TARGET_COLUMN
from laptop_project.logger import logging
import sys
import pandas as pd
from typing import Optional
from dataclasses import dataclass
from laptop_project.entity.estimator import LaptopModel
from laptop_project.constants import PARAMS_FILE_PATH
from laptop_project.utils.main_utils import load_numpy_array_data, read_yaml_file, load_object, save_object
from catboost import CatBoostRegressor


import dagshub
dagshub.init(repo_owner='nikhil.sonkusare94', repo_name='Laptop-Price-Calculator', mlflow=True)


class ModelEvaluation:

    def __init__(self, model_eval_config: ModelEvaluationConfig, data_ingestion_artifact: DataIngestionArtifact,
                 model_trainer_artifact: ModelTrainerArtifact):
        try:
            self.model_eval_config = model_eval_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.model_trainer_artifact = model_trainer_artifact
            self._param_config = read_yaml_file(file_path=PARAMS_FILE_PATH)
        except Exception as e:
            raise LaptopException(e, sys) from e


    def evaluate_model(self) :
        """
        Method Name :   evaluate_model
        Description :   This function is used to evaluate trained model 
                        with production model and choose best model 
        
        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            x, y = test_df.drop(TARGET_COLUMN, axis=1), test_df[TARGET_COLUMN]

            trained_model = load_object(file_path=self.model_trainer_artifact.trained_model_file_path)
           
            
            with mlflow.start_run():
                y_pred = trained_model.predict(x)
            
                r2 = r2_score(y, y_pred) 
                mse = mean_squared_error(y, y_pred)  
                mae = mean_absolute_error(y, y_pred)  
                metric_artifact = RegressionMetricArtifact(r2_score=r2, mae_score=mae, mse_score=mse)

                mlflow.log_params(self._param_config)
                mlflow.log_metric('r2_score', r2)
                mlflow.log_metric('mse_score', mse)
                mlflow.log_metric('mae_score', mae)
                # mlflow.catboost.log_model("model", CatBoostRegressor())

            metric_artifact = RegressionMetricArtifact(r2_score=r2, mae_score=mae, mse_score=mse)
            logging.info(f"Metric Artifact: {metric_artifact}")
            return metric_artifact

        except Exception as e:
            raise LaptopException(e, sys)

    def initiate_model_evaluation(self):
        """
        Method Name :   initiate_model_evaluation
        Description :   This function is used to initiate all steps of the model evaluation
        
        Output      :   Returns model evaluation artifact
        On Failure  :   Write an exception log and then raise an exception
        """  
        try:
            evaluate_model_response = self.evaluate_model()

            model_evaluation_artifact = ModelEvaluationArtifact(
                trained_model_path=self.model_trainer_artifact.trained_model_file_path,
                
            )

            logging.info(f"Model evaluation artifact: {model_evaluation_artifact}")
            return model_evaluation_artifact
        except Exception as e:
            raise LaptopException(e, sys) from e