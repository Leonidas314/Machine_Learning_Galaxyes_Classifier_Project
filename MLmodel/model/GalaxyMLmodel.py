import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
import seaborn as sns

path_training_solutions = os.path.join("..", "dataset", "training_solutions_rev1.csv")
df_train = pd.read_csv(path_training_solutions)

print(f"Datos cargados: {df_train.shape[0]} galaxias, {df_train.shape[1]} columnas")
print(f"Formato: GalaxyID + {df_train.shape[1]-1} probabilidades morfológicas")

prob_columns = [col for col in df_train.columns if col != 'GalaxyID']

path_training = os.path.join("..", "dataset", "images_training_rev1")
path_test = os.path.join("..", "dataset", "images_test_rev1")

print(f"\n  VERIFICANDO IMÁGENES:")
train_images = os.listdir(path_training) if os.path.exists(path_training) else []
test_images = os.listdir(path_test) if os.path.exists(path_test) else []
    
print(f"Imágenes de entrenamiento: {len(train_images)}")
print(f"Imágenes de test: {len(test_images)}")

mean_probs = df_train[prob_columns].mean().sort_values(ascending=False)
print("Top 10 categorías más frecuentes:")
for i, (col, prob) in enumerate(mean_probs.head(10).items()):
    print(f"  {i+1:2d}. {col}: {prob:.4f}")    
