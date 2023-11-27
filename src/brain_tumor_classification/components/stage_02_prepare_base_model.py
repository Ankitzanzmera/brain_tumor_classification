import tensorflow as tf
from brain_tumor_classification.entity.config_entity import PrepareBaseModelConfig
from brain_tumor_classification.utils.logger import logger

class PrepareBaseModel:
    def __init__(self,config:PrepareBaseModelConfig) -> None:
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.applications.VGG16(
            weights=self.config.params_weights,
            include_top = self.config.params_include_top,
            input_shape = self.config.params_image_size
        )
        
        self.model.save(self.config.base_model_path)
    
    @staticmethod
    def _prepare_full_model(model:tf.keras.models,classes:int,learning_rate: float,freeze_all: bool):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        for layer in model.layers:
            print(layer.name,layer.trainable)
        
        full_model = tf.keras.models.Sequential()
        full_model.add(model)
        full_model.add(tf.keras.layers.Flatten())
        full_model.add(tf.keras.layers.Dense(256,activation = 'relu'))
        full_model.add(tf.keras.layers.Dense(units = classes,activation = 'softmax'))


        full_model.compile( 
            optimizer = tf.keras.optimizers.Adam(learning_rate = learning_rate),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ['accuracy']
            )

        full_model.summary()
        return full_model

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            learning_rate = self.config.params_learning_rate,
            freeze_all = True
        )
        self.full_model.save(self.config.updated_base_model_path)