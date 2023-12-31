from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source: str
    local_data_file:Path
    unzip_dir:Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir:Path
    base_model_path:Path
    updated_base_model_path:Path
    params_image_size:list
    params_weights: str
    params_include_top:bool
    params_classes: int
    params_learning_rate:float

@dataclass(frozen=True)
class PrepareCallbackConfig:
    root_dir:Path
    tensorboard_log_dir:Path
    checkpoint_model_path: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model:Path
    training_data:Path
    validation_data:Path
    params_is_augmentation:bool
    params_image_size: list
    params_batch_size: int
    params_epochs: int

@dataclass(frozen=True)
class ModelEvaluateConfig:
    path_of_model:Path
    test_data_path:Path
    params_batch_size:int
    params_image_size:list