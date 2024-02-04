import threading
from flask import Flask, request, jsonify, render_template,send_from_directory 
from PIL import Image  
import torch  
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import transforms
from torchvision.models import resnet50
from sklearn.preprocessing import LabelEncoder
import numpy as np
import os
import base64

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
# clase contro con metodos para el procesamiento de imagenes para utilizar con pytorch
from control import cargar_y_preprocesar_imagen_pytorch, calcular_similitud_pytorch,predecir_hojas_pytorch

#-----------------------------------------------------------------------------------------

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# encoder de las clases
clases_encoder = np.load('F:/Universidad/FlaskIntro/FlaskDeepLeaves/encoder_classes.npy')
encoder = LabelEncoder()
encoder.classes_ = clases_encoder

# Ruta relativa a la carpeta de imágenes
image_absolute = os.path.abspath('F:/Universidad/ProyectoDeepleaves/ImagenesStatic')  
images_path = image_absolute
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
# Cargar imágenes y generar datos de entrenamiento
X_data = []
Y_data = []

for filename in os.listdir(images_path):
    image_path = os.path.join(images_path, filename)
    image = cargar_y_preprocesar_imagen_pytorch(image_path)
    if image is not None:
        X_data.append(image)
        img_name = filename.split('.')[0]
        Y_data.append(img_name)

# Convertir las listas a tensores de PyTorch
# Crear un diccionario que mapea cada etiqueta única a un índice numérico
etiqueta_a_indice = {etiqueta: indice for indice, etiqueta in enumerate(set(Y_data))}

# Crear una lista de índices numéricos correspondientes a las etiquetas
Y_data_numerico = [etiqueta_a_indice[etiqueta] for etiqueta in Y_data]

# Convertir la lista de índices a un tensor de PyTorch
Y_data_tensor = torch.tensor(Y_data_numerico)        

X_data = torch.stack(X_data)
# Y_data = torch.tensor(Y_data)

# Aplanar las imágenes
X_data_flatten = X_data.view(len(X_data), -1).numpy() / 255.0
#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------

#  Crear una instancia de QApplication antes de cualquier ventana o widget de PyQt5
#app_qt = QApplication([])

# Instancia de la clase predictora de hojas
#predictor_hojas = PredictorHojasPyTorch()

# Función para ejecutar el bucle de eventos de PyQt5 en un hilo separado
# def run_qt_app():
#     app_qt.exec_()

# Hilo para ejecutar la aplicación de PyQt5
# qt_thread = threading.Thread(target=run_qt_app)
# qt_thread.start()

#-----------------------------------------------------------------------------------------
# aplicacion flask
app = Flask(__name__)

# carga del modelo de pytroch
modelo = resnet50(pretrained=False)
num_ftrs = modelo.fc.in_features
modelo.fc = nn.Linear(num_ftrs, 5) # ajustar el numero de clases si es necesario con el conjunto de datos
modelo_resnet50 ='F:/Universidad/ProyectoDeepleaves/ModeloPytorch/resnet50.pth'
modelo.load_state_dict(torch.load(modelo_resnet50,map_location=torch.device('cpu')))
modelo = modelo.to(device)
modelo.eval()

class_names = ['Borojo', 'Carambolo', 'Guanabano', 'Naranjo común', 'Palma de yuca']



@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, 'icons/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/infoPl')
def infoPl():
    return render_template('infoPl.html')

@app.route('/')
def about():
    return render_template('/about.html')

@app.route('/red')
def redNeur():
    return render_template('red.html')


@app.route('/capturar_foto', methods=['POST'])
def capturar_foto():
    data = request.get_json()
    if 'photo' in data:
        photo_data = data['photo']
        
        # Guardar la foto temporalmente
        temp_filename = 'temp_captured_image.png'
        with open(temp_filename, 'wb') as f:
            # Decodificar la cadena base64 y escribir en el archivo
            f.write(base64.b64decode(photo_data.split(',')[1]))


        # Realizar la predicción usando el código existente
        # hojas_predichas = predictor_hojas.cargar_imagen(temp_filename)
        # predictor_hojas.predecir_hojas()  
        hojas_predichas = predecir_hojas_pytorch(temp_filename,modelo)

        # Calcular similitudes y obtener las 2 especies de hojas más similares
        similitudes = calcular_similitud_pytorch(temp_filename,modelo,X_data_flatten)
        indices_similares = np.argsort(similitudes)[::-1][:2]
        hojas_similares = [Y_data[idx] for idx in indices_similares]

        # Eliminar la foto temporal
        os.remove(temp_filename)

        return jsonify({'nombre_hojas': hojas_predichas, 'hojas_similares': hojas_similares})
    else:
        return jsonify({'error': 'No se proporcionó una foto válida.'})

@app.route('/predict', methods = ['POST'])
def predict_hojas():
    data = request.files['imagen_prediccion']
    if data:
        # Guardar la imagen temporalmente
        temp_filename = 'temp_image.jpg'
        data.save(temp_filename)

        # Realizar la predicción usando el código existente
        # hojas_predichas = predictor_hojas.cargar_imagen(temp_filename)
        # predictor_hojas.predecir_hojas()
        hojas_predichas = predecir_hojas_pytorch(temp_filename,modelo)

        # Calcular similitudes y obtener las 2 especies de hojas más similares
        similitudes = calcular_similitud_pytorch(temp_filename,modelo,X_data_flatten)
        indices_similares = np.argsort(similitudes)[::-1][:2]
        hojas_similares = [Y_data_tensor[idx] for idx in indices_similares]

        # Eliminar la imagen temporal
        os.remove(temp_filename)

        return jsonify({'nombre_hojas': hojas_predichas, 'hojas_similares': hojas_similares})
    else:
        return jsonify({'error': 'No se proporcionó una imagen válida.'})



if __name__ == '__main__':
    #inicio de la aplicacion en flask
    app.run(debug=True)

    # Esperar a que el hilo de PyQt5 termine antes de salir
    #qt_thread.join()