import sys
import tensorflow as tf
from brain_tumor_classification.entity.config_entity import ModelTrainingConfig
from brain_tumor_classification.utils.exception import CustomException

class ModelTraining:
    def __init__(self,config:ModelTrainingConfig) -> None:
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model)
    
    def train_valid_generator(self):
        try:
            if self.config.params_is_augmentation: 
                train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                    rescale = 1./255,
                    shear_range = 0.2,
                    zoom_range = 0.2,
                    horizontal_flip = True
                )
                valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                    rescale = 1./255
                )
            else:
                train_datagenerator = valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                    rescale = 1./255
                )

            data_flow_kwargs = dict(
                target_size = self.config.params_image_size[:-1],
                batch_size = self.config.params_batch_size,
                class_mode = 'categorical',
            )
            self.training_data = train_datagenerator.flow_from_directory(
                directory = self.config.training_data,
                **data_flow_kwargs
            )

            self.validation_data = valid_datagenerator.flow_from_directory(
                directory = self.config.validation_data,
                **data_flow_kwargs
            )
            
        except Exception as e:
            raise CustomException(e,sys)

    def train_model(self,callbacks_list: list):
        self.steps_per_epochs = self.training_data.samples // self.training_data.batch_size
        self.validation_steps = self.validation_data.samples //self.validation_data.batch_size 

        self.model.fit(
            self.training_data,
            validation_data = self.validation_data,
            epochs = self.config.params_epochs,
            steps_per_epoch = self.steps_per_epochs,
            validation_steps = self.validation_steps,
            callbacks = callbacks_list
        )

        self.model.save(self.config.trained_model_path)