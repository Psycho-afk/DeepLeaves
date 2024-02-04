import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import resnet50
from torchvision.transforms import v2 as transforms
from PIL import Image
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os


#Nueva ruta de imagenes dentro del proyecto
# images_folder = "static/static_images"
# static_base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
# images_path = os.path.join(static_base_path, images_folder)

images_folder = "static_images"
images_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), images_folder)
# image_absolute = os.path.abspath('F:\\Universidad\\FlaskIntro\\FlaskDeepLeaves\\static_images')
# images_path = image_absolute



print(f"Constructed path for images: {images_path}")


# Más impresiones para identificar dónde se detiene la ejecución
print("Antes del modelo")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# carga del modelo de pytroch resnet50
modelo = resnet50(weights=None)
num_ftrs = modelo.fc.in_features
modelo.fc = nn.Linear(num_ftrs, 5) # ajustar el numero de clases si es necesario con el conjunto de datos
modelo_resnet50 ='./Modelos/resnet50.pth' # modelo del 22/01/2024
modelo.load_state_dict(torch.load(modelo_resnet50,map_location=torch.device('cpu')))
modelo = modelo.to(device)
modelo.eval()


class_names = ['Borojo', 'Carambolo', 'Guanabano', 'Naranjo común', 'Palma de yuca']

# Transformaciones para las imágenes
transform = transforms.Compose([
    transforms.ToImage(),
    transforms.Resize((224, 224)),
    transforms.ToDtype(torch.float32, scale=True),
    transforms.Lambda(lambda x: x[:3, :, :]),  # Eliminar el canal alfa (si existe)
])

# Ruta relativa a la carpeta de imágenes
# image_absolute = os.path.abspath('F:/Universidad/ProyectoDeepleaves/ImagenesStatic')  
# images_path = image_absolute




# #------------------ mobielnetv2---------------------------------
#--------------------------------------------



# Función para extraer características de una imagen funcion original
# def extract_features(img):

#     try:
#         print(f"Intentando extraer características de la imagen.")
        
#         if isinstance(img, str):  # Si es una ruta de archivo, abre la imagen
#             img = Image.open(img)
        
#         img = transform(img)
#         img = img.unsqueeze(0)

#         with torch.no_grad():
#             features = modelo(img)
#             print(f"Features extracted: {features}")
    
#         return features.numpy().flatten()  # Devuelve las características como un arreglo numpy

#     except Exception as e:
#         print(f"Error al abrir o procesar la imagen: {str(e)}")
#         raise

# Función para realizar la predicción
#Funcion original sin modificaciones que funciona    
# def predict_hojas(image_path):
#     print(f"Images path: {images_path}")

#     img = Image.open(image_path)
#     target_features = extract_features(img)  # Extrae características directamente desde la imagen
#     img = transform(img)
#     img = img.unsqueeze(0)

#     with torch.no_grad():
#         output = modelo(img)
#         _, predicted_class = torch.max(output, 1)
        

#     return predicted_class.item(), target_features

#--------------- funcion predict de prueba
def predict_hojas(image_path):
    print(f"Images path: {images_path}")
    constructed_path = os.path.join(images_path, image_path)
    print(f"Constructed path for images: {constructed_path}")

    try:
        print(f"Intentando abrir la imagen: {image_path}")

        # Cargar la imagen desde la ruta
        img = Image.open(image_path)

        # Extraer características
        target_features = extract_features(img)
        target_features = target_features[0]  # Tomar la primera fila del array NumPy
        print(f"Features extracted: {target_features}")
        print(f"Target features shape: {target_features.shape}")
        print(f"Features type: {type(target_features)}")

        # Resto del código de predicción...
        img = transform(img).to(device)
        img = img.unsqueeze(0)

        with torch.no_grad():
            output = modelo(img)
            _, predicted_class = torch.max(output, 1)

        return predicted_class.item(), target_features.tolist()

    except Exception as e:
        error_message = f"Error en la predicción: {str(e)}"
        print(error_message)
        raise

#funcion extraxt features prueba
def extract_features(img):
    try:
        print(f"Intentando extraer características de la imagen.")
        
        if isinstance(img, str):  # Si es una ruta de archivo, abre la imagen
            img = Image.open(img).convert("RGB")
        
        img = transform(img).to(device)
        img = img.unsqueeze(0).to(device)

        with torch.no_grad():
            features = modelo(img)
            print(f"Features extracted: {features}")
            print(f"Features shape: {features.shape}")

        if features.shape != (1, 5):
            raise ValueError(f"Dimensiones inesperadas de las características: {features.shape}")

        return features.cpu().numpy()  # Devuelve las características como un arreglo numpy

    except Exception as e:
        print(f"Error al abrir o procesar la imagen: {str(e)}")
        raise


#-------------------------------------------------
# Función para obtener las hojas más similares
#funcion anterior
# def get_similar_leaves(target_features,class_names, threshold=0.5):
#     similar_leaves = []

#     static_base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')

#         # Verificar si el directorio 'static' existe
#     if os.path.exists(static_base_path):
#         print("Base static folder exists!")
#     else:
#         print("Base static folder does not exist!")

#     print(f"Target Features: {target_features}")

#     for class_name in class_names:

#         class_folder = os.path.join(static_base_path, 'static_images', class_name)
#         print(f"Class folder: {class_folder}")
#         # Verificar si la carpeta existe
#     if os.path.exists(class_folder):
#         print(f"Class folder {class_name} exists!")
#     else:
#         print(f"Class folder {class_name} does not exist!")

#         print(f"Constructed path for {class_name}: {class_folder}")    

#         try:

#             for filename in os.listdir(class_folder):
#                 if filename.endswith(('.jpg', '.png', '.jpeg','.JPG')):
#                     leaf_path = os.path.join(class_folder, filename)
#                     leaf_features = extract_features(leaf_path)

#                     # Calcular similitud coseno
#                     similarity = cosine_similarity([target_features], [leaf_features])[0][0]
#                     print(f"Leaf: {filename}, Similarity: {similarity}")

#                     if similarity > threshold:
#                         similar_leaves.append({"class": class_name, "filename": filename, "similarity": similarity})
#                         print(f"Similar leaf found: {filename} in class {class_name} with similarity {similarity}")
#         except Exception as e:  
#              print(f"Error al acceder a la carpeta {class_folder}: {str(e)}")         
#     return similar_leaves



#funcion de prueba
# Función para obtener las hojas más similares
def get_similar_leaves(target_features_list, class_names, threshold=0.5):
      
    similar_leaves = []

    for class_name in class_names:
        class_folder = os.path.join(images_path, class_name)
        print(f"Class folder: {class_folder}")

        if not os.path.exists(class_folder):
            print(f"Folder does not exist!")
            continue

        for filename in os.listdir(class_folder):
            print("class name: ", class_name)
            if filename.endswith(('.jpg', '.png', '.jpeg', '.JPG')):
                leaf_path = os.path.join(class_folder, filename)
                print(f"Leaf path: {leaf_path}")
                leaf_features = extract_features(leaf_path).flatten().tolist()
                print("class name: ", class_name)
                # Añadimos una verificación para las dimensiones de las características
                if leaf_features.shape != (5,):
                    raise ValueError(f"Dimensiones inesperadas de las características de la hoja {filename}: {leaf_features.shape}")

                # Calcular similitud coseno
                similarity = cosine_similarity([target_features_list], [leaf_features])[0][0]
                print("class name: ", class_name)
                if similarity > threshold:
                    similar_leaves.append({"class": class_name, "filename": filename, "similarity": similarity})

    return similar_leaves




