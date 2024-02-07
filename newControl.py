import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import resnet50
from torchvision import transforms
from PIL import Image
import numpy as np
import cv2
from sklearn.metrics.pairwise import cosine_similarity
import os



images_folder = "static_images"
images_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), images_folder)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# carga del modelo de pytroch resnet50
modelo = resnet50(pretrained=False)
num_ftrs = modelo.fc.in_features
modelo.fc = nn.Linear(num_ftrs, 5) # ajustar el numero de clases si es necesario con el conjunto de datos
modelo_resnet50 ='F:/Universidad/ProyectoDeepleaves/ModeloPytorch/resnet50.pth' # modelo del 22/01/2024
modelo.load_state_dict(torch.load(modelo_resnet50,map_location=torch.device('cpu')))
modelo = modelo.to(device)
modelo.eval()


class_names = ['Borojo', 'Carambolo', 'Guanabano', 'Naranjo común', 'Palma de yuca']

# Transformaciones para las imágenes
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Lambda(lambda x: x[:3, :, :]),  # Eliminar el canal alfa (si existe) esto se realiza, ya que
    #la imagen que se captura desde la camara trae 4 canales y el modelo solo admite 3
])






# #------------------ mobielnetv2---------------------------------
#--------------------------------------------

#--------------- funcion predictora de hojas
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
        #target_features = target_features[0]  # Tomar la primera fila del array NumPy
        target_features_flat = target_features.flatten().tolist()  # Convertir a lista plana
        print(f"Features extracted: {target_features}")
        print(f"Target features shape: {target_features.shape}")
        print(f"Features type: {type(target_features)}")

        # Resto del código de predicción...
        img = transform(img)
        img = img.unsqueeze(0)

        with torch.no_grad():
            output = modelo(img)
            _, predicted_class = torch.max(output, 1)

        return predicted_class.item(), target_features_flat

    except Exception as e:
        error_message = f"Error en la predicción: {str(e)}"
        print(error_message)
        raise

#funcion para extraer caracteristicas de la imagen
def extract_features(img):
    try:
        print(f"Intentando extraer características de la imagen.")
        
        if isinstance(img, str):  # Si es una ruta de archivo, abre la imagen
            img = Image.open(img).convert("RGB")
        
        img = transform(img)
        img = img.unsqueeze(0)

        with torch.no_grad():
            features = modelo(img)
            print(f"Features extracted: {features}")
            print(f"Features shape: {features.shape}")

        if features.shape != (1, 5):
            raise ValueError(f"Dimensiones inesperadas de las características: {features.shape}")

        
        return features # retorna el tensor

    except Exception as e:
        print(f"Error al abrir o procesar la imagen: {str(e)}")
        raise


#-------------------------------------------------
# Función para obtener las hojas más similares
def get_similar_leaves(target_features, class_names, threshold=0.5):
      
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
                print("class name- primer if despues del for: ", class_name)
                
                if len(leaf_features) != len(target_features):
                    print(f"Dimensiones inesperadas de las características de la hoja {filename}")
                    print(f"Target Features Shape: {len(target_features)}")
                    print(f"Leaf Features Shape: {len(leaf_features)}")
                    continue

                print(f"Target Features: {target_features}")
                print(f"Leaf Features: {leaf_features}")
                

                try:
                    # Calcular similitud coseno
                    #similarity = cosine_similarity([target_features], [leaf_features])[0][0]
                    similarity = np.dot(target_features, leaf_features) / (np.linalg.norm(target_features) * np.linalg.norm(leaf_features))
                    print(f"Similarity with {filename}: {similarity}")
                    if similarity > threshold:
                
                        similar_leaves.append({"class": class_name, "filename": filename, "similarity": similarity})
                except Exception as e:
                    print(f"Error calculando la similitud: {str(e)}")

    return similar_leaves




