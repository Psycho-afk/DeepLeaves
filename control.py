import cv2
import torch
from torchvision import transforms
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
from PIL import Image
import numpy as np

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt



# encoder de las clases
clases_encoder = np.load('F:/Universidad/FlaskIntro/FlaskDeepLeaves/encoder_classes.npy')
encoder = LabelEncoder()
encoder.classes_ = clases_encoder


#--------------------------------------------------------------------------------
# metodo original
# def cargar_y_preprocesar_imagen_pytorch(ruta_imagen):
#     imagen = cv2.imread(ruta_imagen)
#     if imagen is not None:

#         imagen_redimensionada = cv2.resize(imagen, (28, 28))

#         # Convertir la imagen de NumPy a un tensor de PyTorch
#         imagen_tensor = torch.from_numpy(imagen_redimensionada).permute(2, 0, 1).float() / 255.0

#         # Convertir el tensor de PyTorch a un array de NumPy antes de la transformación
#         imagen_numpy = imagen_tensor.numpy()

#         # Convertir el array de NumPy a una imagen PIL
#         imagen_pil = Image.fromarray((imagen_numpy * 255).astype('uint8').transpose((1, 2, 0)))

#         transform = transforms.Compose([
#             transforms.Resize((224,224)),
#             transforms.ToTensor(),
           
#         ])

#         imagen_preprocesada = transform(imagen_pil).unsqueeze(0)

#         return imagen_preprocesada
#     else:
#         return None
    
def cargar_y_preprocesar_imagen_pytorch(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)
    if imagen is not None:
        # Asegúrate de que la imagen tiene tres canales (RGB)
        if imagen.shape[2] == 3:
            # Redimensiona la imagen a las dimensiones esperadas por ResNet50
            imagen_redimensionada = cv2.resize(imagen, (224, 224))

            # Convertir la imagen de NumPy a un tensor de PyTorch
            imagen_tensor = torch.from_numpy(imagen_redimensionada).permute(2, 0, 1).float() / 255.0
        
           # Normalizar la imagen utilizando medias y desviaciones estándar específicas de ImageNet
            mean = torch.tensor([0.485, 0.456, 0.406])
            std = torch.tensor([0.229, 0.224, 0.225])
            imagen_normalizada = transforms.functional.normalize(imagen_tensor, mean, std)
        
            # Añadir una dimensión adicional para representar el lote (batch)
            imagen_preprocesada = imagen_normalizada.unsqueeze(0)

            # Convertir el tensor de tipo Byte a Float
            imagen_preprocesada = imagen_preprocesada.float()

            return imagen_preprocesada
        else:
            print("La imagen no tiene tres canales RGB.")
            return None
    else:
        print("No se pudo leer la imagen.")
        return None



# metodo original
# def calcular_similitud_pytorch(ruta_imagen, modelo, X_data_flatten):
#     imagen_preprocesada = cargar_y_preprocesar_imagen_pytorch(ruta_imagen)
    
#     if imagen_preprocesada is not None:
#         with torch.no_grad():
#             salida_modelo = modelo(imagen_preprocesada.view(1, -1))
        
#         similitudes = cosine_similarity(salida_modelo.numpy(), X_data_flatten)
#         return similitudes[0]
#     else:
#         return None

#metodo para debug
# def calcular_similitud_pytorch(ruta_imagen, modelo, X_data_flatten):
#     imagen_preprocesada = cargar_y_preprocesar_imagen_pytorch(ruta_imagen)
    
#     if imagen_preprocesada is not None:
#         with torch.no_grad():
#             modelo.eval()
#             salida_modelo = modelo(imagen_preprocesada.view(1, 3, 224, 224))
        
        
#         similitudes = cosine_similarity(salida_modelo.reshape(1,-1), X_data_flatten.reshape(1,-1))
        
#         salida_modelo_np = salida_modelo.detach().cpu().numpy().flatten()

#         print("Dimensiones de salida_modelo:", salida_modelo.detach().numpy().shape)
#         print("Dimensiones de X_data_flatten:", X_data_flatten.shape)
#         print("Dimensiones de salida_modelo_np:", salida_modelo_np.shape)


#         return similitudes[0]
#     else:
#         return None    

#metodo para depurar el error    

def calcular_similitud_pytorch(ruta_imagen, modelo, X_data_flatten):
    imagen_preprocesada = cargar_y_preprocesar_imagen_pytorch(ruta_imagen)
    
    if imagen_preprocesada is not None:
        with torch.no_grad():
            salida_modelo = modelo(imagen_preprocesada.view(1, 3, 224, 224))

        # Aplana la salida_modelo de manera correcta
        salida_modelo_flatten = salida_modelo.view(1, -1).detach().numpy()

        print("Dimensiones de salida_modelo_flatten:", salida_modelo_flatten.shape)
        print("Dimensiones de X_data_flatten:", X_data_flatten.shape)

        # Normaliza los datos antes de calcular la similitud
        salida_modelo_flatten_normalized = salida_modelo_flatten / np.linalg.norm(salida_modelo_flatten)
        X_data_flatten_normalized = X_data_flatten / np.linalg.norm(X_data_flatten, axis=1, keepdims=True)

        print("Dimensiones de salida_modelo_flatten_normalized:", salida_modelo_flatten_normalized.shape)
        print("Dimensiones de X_data_flatten_normalized:", X_data_flatten_normalized.shape)

        # Reorganiza las dimensiones para evitar problemas de alineación
        salida_modelo_flatten_normalized = salida_modelo_flatten_normalized.reshape(1, -1)
        X_data_flatten_normalized = X_data_flatten_normalized.reshape(1, -1)

        print("Dimensiones de salida_modelo_flatten_normalized (reshaped):", salida_modelo_flatten_normalized.shape)
        print("Dimensiones de X_data_flatten_normalized (reshaped):", X_data_flatten_normalized.shape)


        # Calcular la similitud del coseno manualmente
        similitud = np.dot(salida_modelo_flatten_normalized, X_data_flatten_normalized.T)

        return similitud[0]  # Tomamos el primer elemento del resultado
    else:
        return None















# def predecir_hojas_pytorch(ruta_imagen, modelo):
#     imagen_preprocesada = cargar_y_preprocesar_imagen_pytorch(ruta_imagen)
    
#     if imagen_preprocesada is not None:

#         imagen_preprocesada = imagen_preprocesada.unsqueeze(0)

#         with torch.no_grad():
#             probabilidades_prediccion = modelo(imagen_preprocesada)
        
#         indice_clase_predicha = torch.argmax(probabilidades_prediccion).item()
#         hojas_predichas = encoder.inverse_transform([indice_clase_predicha])[0]
        
#         return hojas_predichas
#     else:
#         return "No se pudo cargar la imagen."
    

def predecir_hojas_pytorch(ruta_imagen, modelo):
    imagen_preprocesada = cargar_y_preprocesar_imagen_pytorch(ruta_imagen)
    
    if imagen_preprocesada is not None:
        with torch.no_grad():
            # Elimina la dimensión adicional [1] antes de pasar al modelo
            salida_modelo = modelo(imagen_preprocesada)

        probabilidades_prediccion = torch.nn.functional.softmax(salida_modelo, dim=1)
        indice_clase_predicha = torch.argmax(probabilidades_prediccion).item()
        hojas_predichas = encoder.inverse_transform([indice_clase_predicha])[0]
        
        return hojas_predichas
    else:
        return "No se pudo cargar la imagen."

#--------------------------------------------------------------------------------


