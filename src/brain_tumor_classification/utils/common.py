import os,sys
from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
import json
from brain_tumor_classification.utils.exception import CustomException


@ensure_annotations
def create_directories(path_to_directories:list):
    """
        Creates list of Direcory

        input: List of Path to create directory
        return: Nothing

    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
        Reads YAML File

        input: Path of Yaml File
        return: return Configbox in which have ontent of Yaml file
    """

    try:
        with open(path_to_yaml,"r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('Yaml Is Empty')
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def get_size(path:Path) -> str:
    """ 
        Gives The size of File in KB

        input : Path of File
        return : Return string having Size in MB KB of File
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def save_json(path: Path,data: dict):
    """ 
        Save The Json Data

        input: Path of file and Data to write

    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)