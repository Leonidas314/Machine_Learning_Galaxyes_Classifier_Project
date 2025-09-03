import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image
from tensorflow import keras
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
import seaborn as sns

# Rutas
dataset_dir = Path("..") / "dataset"
path_training_solutions = dataset_dir / "training_solutions_rev1.csv"
path_training_images = dataset_dir / "images_training_rev1"
path_test_images = dataset_dir / "images_test_rev1"

# Cargar CSV
training_solutions = pd.read_csv(path_training_solutions)
print(f"Datos cargados: {training_solutions.shape[0]} galaxias, {training_solutions.shape[1]} columnas")
print(f"Formato: GalaxyID + {training_solutions.shape[1] - 1} probabilidades morfológicas")

prob_columns = [col for col in training_solutions.columns if col != 'GalaxyID']

# Verificar imágenes
print(f"\n  VERIFICANDO IMÁGENES:")
train_images = list(path_training_images.iterdir()) if path_training_images.exists() else []
test_images = list(path_test_images.iterdir()) if path_test_images.exists() else []

print(f"Imágenes de entrenamiento: {len(train_images)}")
print(f"Imágenes de test: {len(test_images)}")

# Top categorías
mean_probs = training_solutions[prob_columns].mean().sort_values(ascending=False)
print("Top 10 categorías más frecuentes:")
for i, (col, prob) in enumerate(mean_probs.head(10).items()):
    print(f"  {i+1:2d}. {col}: {prob:.4f}")

# Parámetros
IMG_SIZE = 64
BATCH_SIZE = 32
NUM_CLASSES = len(prob_columns)

# Función de preprocessing
def preprocess_image(img_path: Path):
    if not img_path.exists():
        raise FileNotFoundError(f"No existe el archivo: {img_path}")
    print(f"Abriendo: {img_path}")
    img = Image.open(img_path).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))
    return np.array(img) / 255.0

# Cargar dataset
def load_dataset(image_folder: Path, solutions_df, prob_columns):
    images = []
    labels = []

    for _, row in solutions_df.iterrows():
        galaxy_id = f"{int(row['GalaxyID'])}.jpg"
        img_path = image_folder / galaxy_id

        if img_path.exists():
            images.append(preprocess_image(img_path))
            labels.append(row[prob_columns].values)
        else:
            print(f"Imagen no encontrada: {img_path}")

    X = np.array(images, dtype=np.float32)
    y = np.array(labels, dtype=np.float32)
    return X, y

print("Cargando dataset de entrenamiento...")
X, y = load_dataset(path_training_images, training_solutions, prob_columns)
print(f"Dataset cargado: {X.shape[0]} imágenes, tamaño {X.shape[1:]}")

# (scikit learn) Divide el dataset para evaluarse durante el entrenamiento
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# modelo CNN
model = models.Sequential([
    layers.Input(shape=(IMG_SIZE, IMG_SIZE, 3)),

    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, (3, 3), activation='relu'),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),

    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(NUM_CLASSES, activation='sigmoid')  # usamos sigmoid porque cada columna es una probabilidad
])

# -------------------------------
# Compilacion
model.compile(optimizer='adam',
              loss='binary_crossentropy',  # como son probabilidades multilabel
              metrics=['accuracy'])

# -------------------------------
# Resumen
model.summary()

# -------------------------------
# Entrenamiento
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    batch_size=BATCH_SIZE,
    epochs=20
)

model.save("galaxy_model.h5")