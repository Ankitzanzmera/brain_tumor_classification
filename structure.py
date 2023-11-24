import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[ %(asctime)s ] : %(message)s')


project_name = "brain_tumor_classification"
list_of_file = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"templates/index.py",
    f"notebooks/trials.ipynb",
    f"config/config.yaml",
    f"setup.py",
    f"dvc.yaml",
    f"params.yaml",
    f"main.py",
    f"app.py",
    f"requirements.txt"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    dirname,filename = os.path.split(filepath)

    if dirname != "":
        os.makedirs(dirname,exist_ok = True)
        logging.info(f'{dirname} folder is created...')
    
    if (os.path.getsize == 0) or (not os.path.exists(filepath)):
        with open(filepath,"wb"):
            pass
        logging.info(f"{filepath} is created...")
    else:
        logging.info(f"{filepath} Already Exists...")