import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


data_augmentation = keras.Sequential([
    layers.RandomRotation(factor=1.0),  # rotación hasta ±180° (aprox 0-360°)
    layers.RandomTranslation(height_factor=4/424, width_factor=4/424),  # ±4 px
    layers.RandomZoom(height_factor=(-1/1.3 + 1, 1.3 - 1), width_factor=(-1/1.3 + 1, 1.3 - 1)),
    layers.RandomFlip("horizontal")  # flip aleatorio
])

