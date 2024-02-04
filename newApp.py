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

from newControl import predict_hojas, get_similar_leaves,extract_features,class_names


#-----------------------------------------------------------------------------------------



# encoder de las clases
clases_encoder = np.load('F:/Universidad/FlaskIntro/FlaskDeepLeaves/encoder_classes.npy')
encoder = LabelEncoder()
encoder.classes_ = clases_encoder


#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------
# aplicacion flask
app = Flask(__name__, static_folder='static', static_url_path='/static')



@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, 'icons/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/camara')
def camara():
    return render_template('camara.html')

@app.route('/infoPl')
def infoPl():
    return render_template('infoPl.html')

@app.route('/')
def about():
    return render_template('/about.html')

@app.route('/red')
def redNeur():
    return render_template('red.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    if 'file' not in request.files:
        return jsonify({"error": "No se ha proporcionado ninguna imagen."})

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No se ha seleccionado ninguna imagen."})

    try:

        # Guarda el archivo en una ubicación temporal
        temp_file_path = "temp_image.jpg"
        file.save(temp_file_path)

        #obtiene las caracteristicas
        target_features = extract_features(temp_file_path)
        #Realizar predicción
        class_index,target_features_list = predict_hojas(temp_file_path)
        predicted_class_name = class_names[class_index]
        # Encontrar hojas similares
        # Encontrar hojas similares
        similar_leaves = get_similar_leaves(target_features_list, class_names)


        # Elimina el archivo temporal después de su uso
        os.remove(temp_file_path)

        ###------ funciona 
        #class_index, target_features = predict_hojas(file)

        # Mapea el índice predicho al nombre de la hoja
        #predicted_class_name = class_names[class_index]

        # Encuentra hojas similares
        similar_leaves = get_similar_leaves(target_features, class_names)
        ##-----------------------------

        # Devolver resultados en formato JSON
        result = {
            "prediction": f"Predicción: Hoja predicha {predicted_class_name}",
            #"target_features": target_features.tolist(), # Convierte a lista para la respuesta JSON
            #"similar_leaves": similar_leaves
            #"debug_info": "similar_leaves defined" if similar_leaves else "similar_leaves is None"
        }

        #print(result['similar_leaves'])
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": f"Error en la predicción: {str(e)}"})
    

@app.route('/capturar_foto', methods=['POST'])
def capturar_foto():
    try:
        data = request.json
        photo_data = data.get('photo')

        # Guarda el archivo en una ubicación temporal
        temp_file_path = "temp_image.jpg"

        # Decodifica la imagen base64 y guarda en el archivo temporal
        with open(temp_file_path, 'wb') as f:
            f.write(base64.b64decode(photo_data.split(",")[1]))

        # Obtiene las características
        target_features = extract_features(temp_file_path)

        # Realiza la predicción
        class_index, target_features_list = predict_hojas(temp_file_path)
        predicted_class_name = class_names[class_index]

        # Encuentra hojas similares
        similar_leaves = get_similar_leaves(target_features_list, class_names)

        # Elimina el archivo temporal después de su uso
        os.remove(temp_file_path)

        # Devolver resultados en formato JSON
        result = {
            "prediction": f"Predicción: Hoja predicha {predicted_class_name}",
            "similar_leaves": similar_leaves
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": f"Error en la predicción: {str(e)}"})
  


if __name__ == '__main__':
    app.run(debug=True)
