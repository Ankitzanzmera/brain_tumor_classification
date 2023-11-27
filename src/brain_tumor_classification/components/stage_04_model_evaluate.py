from pathlib import Path
import tensorflow as tf
from brain_tumor_classification.utils.common import save_json
from brain_tumor_classification.entity.config_entity import ModelEvaluateConfig

class ModelEvaluate:
    def __init__(self,config:ModelEvaluateConfig) -> None:
        self.config = config

    @property
    def load_model(self) -> tf.keras.models:
        return tf.keras.models.load_model(self.config.path_of_model)
    
    def train_generator(self):
        test_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale = 1./255
        )
        test_data = test_datagenerator.flow_from_directory(
            directory = self.config.test_data_path,
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            class_mode = "categorical"
        )
        return test_data
    
    def evaluate(self):
        self.model = self.load_model
        test_data = self.train_generator()
        self.score = self.model.evaluate(test_data)

    def save_score(self):
        score = {"Loss":self.score[0],"Accuracy":self.score[1]}
        save_json(path = Path("scores.json"),data = score)

