import os
import sys

import numpy as np
import pandas as pd
from laptop_project.entity.config_entity import LaptopPredictorConfig
from laptop_project.entity.s3_estimator import LaptopEstimator
from laptop_project.exception import LaptopException
from laptop_project.logger import logging
from laptop_project.utils.main_utils import read_yaml_file
from pandas import DataFrame


class LaptopData:
    def __init__(self,
                Brand,
                Screen_Size,
                CPU_Model,
                Ram,
                Graphics,
                Disk_Size
                ):
        """
        Laptop Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.Brand = Brand
            self.Screen_Size = Screen_Size
            self.CPU_Model = CPU_Model
            self.Ram = Ram
            self.Graphics = Graphics
            self.Disk_Size = Disk_Size


        except Exception as e:
            raise LaptopException(e, sys) from e

    def get_laptop_input_data_frame(self)-> DataFrame:
        """
        This function returns a DataFrame from USvisaData class input
        """
        try:
            
            laptop_input_dict = self.get_laptop_data_as_dict()
            return DataFrame(laptop_input_dict)
        
        except Exception as e:
            raise LaptopException(e, sys) from e


    def get_laptop_data_as_dict(self):
        """
        This function returns a dictionary from USvisaData class input 
        """
        logging.info("Entered get_usvisa_data_as_dict method as USvisaData class")

        try:
            input_data = {
                "Brand": [self.Brand],
                "Screen_Size": [self.Screen_Size],
                "CPU_Model": [self.CPU_Model],
                "Ram": [self.Ram],
                "Graphics": [self.Graphics],
                "Disk_Size": [self.Disk_Size]
            }

            logging.info("Created laptop data dict")

            logging.info("Exited get_laptop_data_as_dict method as LaptopData class")

            return input_data

        except Exception as e:
            raise LaptopException(e, sys) from e

class LaptopRegressor:
    def __init__(self,prediction_pipeline_config: LaptopPredictorConfig = LaptopPredictorConfig(),) -> None:
        """
        prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            # self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise LaptopException(e, sys)


    def predict(self, dataframe) -> str:
        """
        This is the method of LaptopRegressor
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of LaptopRegressor class")
            model = LaptopEstimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result =  model.predict(dataframe)
            
            return result
        
        except Exception as e:
            raise LaptopException(e, sys)