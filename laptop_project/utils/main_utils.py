import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from laptop_project.exception import LaptopException
from laptop_project.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Load YAML file and return its content as a dictionary.
    
    Parameters:
    file_path (str): Path to the YAML file.
    
    Returns:
    dict: Content of the YAML file as a dictionary.
    """
    logging.info("Entered the read_yaml_file method of utils")

    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise LaptopException(e, sys) from e
    


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Write content to a YAML file.
    
    Parameters:
    file_path (str): Path to the YAML file.
    content (object): Content to write to the YAML file.
    replace (bool, optional): Whether to replace the existing file. Defaults to False.

    Returns:
    None: No return value.
    """
    logging.info("Entered the write_yaml_file method of utils")

    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise LaptopException(e, sys) from e
    



def load_object(file_path: str) -> object:
    """
    Load object from a file using dill.
    
    Parameters:
    file_path (str): Path to the file containing the object.
    
    Returns:
    object: The loaded object.
    """

    logging.info("Entered the load_object method of utils")

    try:

        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise LaptopException(e, sys) from e
    


def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    
    Parameters:
    file_path (str): Path to the file to save the numpy array data.
    array (np.array): Numpy array data to be saved.

    Returns:
    None: No return value.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise LaptopException(e, sys) from e
    



def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    
    Parameters:
    file_path (str): Path to the file containing the numpy array data.
    
    Returns:
    np.array: loaded numpy array data.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise LaptopException(e, sys) from e




def save_object(file_path: str, obj: object) -> None:
    """
    Save object to file
    
    Parameters:
    file_path (str): Path to the file to save the object.
    obj (object): object to be saved.

    Returns:
    None: No return value.
    """

    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise LaptopException(e, sys) from e



def drop_columns(df: DataFrame, cols: list)-> DataFrame:

    """
    drop the columns form a pandas DataFrame
    
    Parameters:
    df (DataFrame): pandas DataFrame from which the columns need to be dropped.
    cols (list): list of columns to be dropped.

    Returns:
    DataFrame: modified DataFrame with specified columns dropped.
    """
    logging.info("Entered drop_columns methon of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        
        return df
    except Exception as e:
        raise LaptopException(e, sys) from e