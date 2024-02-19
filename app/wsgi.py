import threading
from flask import Flask, request, jsonify, render_template,send_from_directory 
from PIL import Image  
from sklearn.preprocessing import LabelEncoder
import torch
import torch.nn as nn
import numpy as np
import os
import base64
from flask_swagger_ui import get_swaggerui_blueprint
from controlResnet50 import predict_hojas, get_similar_leaves,extract_features,class_names



# aplicacion flask
app = Flask(__name__, static_folder='static', static_url_path='/static')

# SWAGGER
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Depp Leaves"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, 'icons/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/prediccion')
def prediccion():
    return render_template('prediccion.html')

@app.route('/redesNeu')
def redesNeu():
    return render_template('redesNeu.html')

@app.route('/camara')
def camara():
    return render_template('camara.html')

@app.route('/infoPl')
def infoPl():
    return render_template('infoPl.html')

@app.route('/')
def home():
    return render_template('/home.html')


@app.route('/predict', methods=['POST'])
def predict_route():
    """
    Endpoint para realizar predicciones de hojas.

    ---
    tags:
      - Predicciones
    responses:
      200:
        description: Predicción exitosa.
        schema:
          properties:
            prediction:
              type: string
              description: Hoja predicha.
            similar_leaves:
              type: array
              description: Lista de hojas similares.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No se ha proporcionado ninguna imagen."})

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No se ha seleccionado ninguna imagen."})

    try:

        # Guarda el archivo en una ubicación temporal
        temp_file_path = "temp_image.jpg"
        file.save(temp_file_path)

        
        #Realizar predicción
        class_index,target_features_list = predict_hojas(temp_file_path)
        predicted_class_name = class_names[class_index]
       
        # Encontrar hojas similares
        similar_leaves = get_similar_leaves(target_features_list, class_names)


        # Elimina el archivo temporal después de su uso
        os.remove(temp_file_path)

        
        ##-----------------------------

        # Devolver resultados en formato JSON
        result = {
            "prediction": f"Predicción: Hoja predicha {predicted_class_name}",
            #"target_features": target_features.tolist(), # Convierte a lista para la respuesta JSON
            "similar_leaves": similar_leaves
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
    #host = '0.0.0.0',port =5000,)
