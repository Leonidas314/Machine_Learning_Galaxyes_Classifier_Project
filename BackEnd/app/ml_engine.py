import tensorflow as tf
import tensorflow.keras as keras   
import numpy as np
from PIL import Image

IMG_SIZE = 64
CLASSES = ["Espiral", "Elíptica", "Irregular"] # Temporal

class MLEngine:
    def __init__(self, model_path="galaxy_model.h5"):
        self.model = tf.keras.models.load_model(model_path)

    def preprocess(self, img: Image.Image):
        img = img.resize((IMG_SIZE, IMG_SIZE))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def predict(self, img: Image.Image):
        x = self.preprocess(img)
        probs = self.model.predict(x)[0]
        idx = np.argmax(probs)
        return CLASSES[idx], float(probs[idx])
