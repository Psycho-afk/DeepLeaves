import os
import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

#TODO Ruta relativa a la carpeta de imágenes (si el código y las imágenes están en el mismo directorio)
images_path = '/Users/giovannyhidalgo/Desktop/MC/archive/images/images/'

# Función para cargar, redimensionar y preprocesar una nueva imagen
def cargar_y_preprocesar_imagen(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)
    if imagen is not None:
        imagen_redimensionada = cv2.resize(imagen, (28, 28))
        imagen_preprocesada = imagen_redimensionada.astype('float32') / 255.0
        return imagen_preprocesada
    else:
        return None

# Función para realizar una predicción de Pokémon a partir de una nueva imagen
def predecir_pokemon(ruta_imagen):
    imagen_preprocesada = cargar_y_preprocesar_imagen(ruta_imagen)
    if imagen_preprocesada is not None:
        imagen_preprocesada = imagen_preprocesada.reshape(1, 28, 28, 3)  # Agregar dimensión del lote (batch) a la imagen
        probabilidades_prediccion = modelo.predict(imagen_preprocesada)
        indice_clase_predicha = np.argmax(probabilidades_prediccion)
        pokemon_predicho = encoder.inverse_transform([indice_clase_predicha])[0]
        return pokemon_predicho
    else:
        return "No se pudo cargar la imagen."

# Función para calcular la similitud entre la imagen cargada y las imágenes de Pokémon en el conjunto de datos
def calcular_similitud(ruta_imagen):
    imagen_preprocesada = cargar_y_preprocesar_imagen(ruta_imagen)
    if imagen_preprocesada is not None:
        imagen_preprocesada = imagen_preprocesada.reshape(1, 28 * 28 * 3)  # Aplanar la imagen
        similitudes = cosine_similarity(imagen_preprocesada, X_data_flatten)
        return similitudes[0]
    else:
        return None

#TODO Cargar el modelo previamente entrenado (Asegúrate de que el modelo y los archivos necesarios estén en las rutas correctas)
modelo = load_model('/Users/giovannyhidalgo/Desktop/MC/model.h5')
clases_encoder = np.load('/Users/giovannyhidalgo/Desktop/MC/encoder_classes.npy')
encoder = LabelEncoder()
encoder.classes_ = clases_encoder

# Cargar imágenes y generar datos de entrenamiento
X_data = []
Y_data = []

for filename in os.listdir(images_path):
    image_path = os.path.join(images_path, filename)
    image = cargar_y_preprocesar_imagen(image_path)
    if image is not None:
        X_data.append(image)
        img_name = filename.split('.')[0]
        Y_data.append(img_name)

X_data_flatten = np.array(X_data).reshape(len(X_data), 28 * 28 * 3).astype('float32') / 255.0

# Crear la aplicación Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_pokemon():
    data = request.files['imagen_prediccion']
    if data:
        # Guardar la imagen temporalmente
        temp_filename = 'temp_image.jpg'
        data.save(temp_filename)

        # Realizar la predicción usando el código existente
        pokemon_predicho = predecir_pokemon(temp_filename)

        # Calcular similitudes y obtener los 5 Pokémon más similares
        similitudes = calcular_similitud(temp_filename)
        indices_similares = np.argsort(similitudes)[::-1][:5]
        pokemon_similares = [Y_data[idx] for idx in indices_similares]

        # Eliminar la imagen temporal
        os.remove(temp_filename)

        return jsonify({'nombre_pokemon': pokemon_predicho, 'pokemon_similares': pokemon_similares})
    else:
        return jsonify({'error': 'No se proporcionó una imagen válida.'})

# Clase PredictorPokemon para la interfaz de PyQt5
class PredictorPokemon(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Predicción de Pokémon')
        self.setGeometry(100, 100, 400, 200)

        self.etiqueta_imagen = QLabel(self)
        self.etiqueta_imagen.setAlignment(Qt.AlignCenter)  # Corregir aquí
        self.etiqueta_imagen.setFixedSize(150, 150)

        self.etiqueta_resultado = QLabel(self)
        self.etiqueta_resultado.setAlignment(Qt.AlignCenter)  # Corregir aquí

        self.boton_cargar = QPushButton('Cargar imagen', self)
        self.boton_cargar.clicked.connect(self.cargar_imagen)

        self.boton_predecir = QPushButton('Predecir', self)
        self.boton_predecir.clicked.connect(self.predecir_pokemon)

        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_imagen)
        layout.addWidget(self.etiqueta_resultado)
        layout.addWidget(self.boton_cargar)
        layout.addWidget(self.boton_predecir)

        self.setLayout(layout)

    def cargar_imagen(self):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.ReadOnly
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, "Cargar imagen", "", "Imágenes (*.png *.jpg *.jpeg)", options=opciones)

        if ruta_imagen:
            self.ruta_imagen = ruta_imagen
            self.mostrar_imagen(ruta_imagen)

    def mostrar_imagen(self, ruta_imagen):
        pixmap = QPixmap(ruta_imagen)
        self.etiqueta_imagen.setPixmap(pixmap.scaled(self.etiqueta_imagen.size(), Qt.KeepAspectRatio))

    def predecir_pokemon(self):
        if hasattr(self, 'ruta_imagen'):
            pokemon_predicho = predecir_pokemon(self.ruta_imagen)
            self.mostrar_resultado(pokemon_predicho)

            similitudes = calcular_similitud(self.ruta_imagen)
            indices_similares = np.argsort(similitudes)[::-1][:5]  # Obtener los 5 Pokémon más similares
            for i, idx in enumerate(indices_similares):
                nombre_pokemon_similar = Y_data[idx]
                porcentaje_similitud = similitudes[idx] * 100
                print(f'Pokémon similar {i + 1}: {nombre_pokemon_similar}, Porcentaje de similitud: {porcentaje_similitud:.2f}%')

    def mostrar_resultado(self, nombre_pokemon):
        self.etiqueta_resultado.setText(f'Pokémon: {nombre_pokemon}')

if __name__ == '__main__':
    app.run(debug=True)