import os
import tensorflow as tf
from datetime import datetime
from brain_tumor_classification.entity.config_entity import PrepareCallbackConfig

class PrepareCallback:
    def __init__(self,config:PrepareCallbackConfig):
        self.config = config

    @property
    def _create_tensorboard(self):
        log_dir_name = f"TB_LOG_at{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}"
        tensorboard_log_dir = os.path.join(self.config.tensorboard_log_dir,log_dir_name)

        return tf.keras.callbacks.TensorBoard(log_dir = tensorboard_log_dir)

    @property
    def _create_model_callback(self):
        return tf.keras.callbacks.ModelCheckpoint(self.config.checkpoint_model_path,save_best_only = True)
    
    def create_TB_CP(self):
        return [self._create_tensorboard,self._create_model_callback]