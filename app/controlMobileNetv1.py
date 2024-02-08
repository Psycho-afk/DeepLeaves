import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.transforms import v2 as transforms
from PIL import Image
import numpy as np
import os

from classMobileNetv1 import MobileNetV1

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

modeloMobileNetv1 = MobileNetV1(num_classes=5, dropout_prob=0.5)    

# modeloMobileNetv1_load = './Modelos/modelo_entrenado_mobilenetv1_norm.pth'

#     # Cargar los parámetros del modelo entrenado
# modeloMobileNetv1.load_state_dict(torch.load(modeloMobileNetv1_load, map_location=torch.device('cpu')))
# modeloMobileNetv1 = modeloMobileNetv1.to(device)

#     # Poner el modelo en modo de evaluación
# modeloMobileNetv1.eval()


images_folder = "static_images"
images_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), images_folder)



class_names_mobileNetv1 = ['Borojo', 'Carambolo', 'Guanabano', 'Naranjo común', 'Palma de yuca']

# Transformaciones para las imágenes
transform = transforms.Compose([
    transforms.ToImage(),
    transforms.Resize((224, 224)),
    transforms.ToDtype(torch.float32, scale=True),
    transforms.Lambda(lambda x: x[:3, :, :]),  # Eliminar el canal alfa (si existe)
])


#--------------- funcion predictora de hoja con el modelo resnet50
def predict_hojas_mobileNetv1(image_path):
    try:
        img = Image.open(image_path)
        img = transform(img).unsqueeze(0)

        with torch.no_grad():
            output = modeloMobileNetv1(img)
            _, predicted_class = torch.max(output, 1)

        return predicted_class.item()

    except Exception as e:
        print(f"Error en la predicción: {str(e)}")
        raise

def extract_features_mobileNetv1(img):
    try:
        img = transform(img).unsqueeze(0)

        with torch.no_grad():
            features = modeloMobileNetv1(img)

        return features

    except Exception as e:
        print(f"Error al abrir o procesar la imagen: {str(e)}")
        raise

def get_similar_leaves_mobileNetv1(target_features, class_names, threshold=0.5):
    similar_leaves = []

    for class_name in class_names:
        class_folder = os.path.join(images_path, class_name)

        if not os.path.exists(class_folder):
            print(f"Folder does not exist!")
            continue

        for filename in os.listdir(class_folder):
            if filename.endswith(('.jpg', '.png', '.jpeg', '.JPG')):
                leaf_path = os.path.join(class_folder, filename)
                print(f"Leaf path: {leaf_path}")
                leaf_features = extract_features_mobileNetv1(leaf_path)
                leaf_features_flat = leaf_features.flatten().tolist()

                if len(leaf_features_flat) != len(target_features):
                    print(f"Dimensiones inesperadas de las características de la hoja {filename}")
                    print(f"Target Features Shape: {len(target_features)}")
                    print(f"Leaf Features Shape: {len(leaf_features_flat)}")
                    continue

                print(f"Target Features: {target_features}")
                print(f"Leaf Features: {leaf_features_flat}")

                try:
                    # Calcular similitud coseno
                    similarity = np.dot(target_features, leaf_features_flat) / (np.linalg.norm(target_features) * np.linalg.norm(leaf_features_flat))
                    print(f"Similarity with {filename}: {similarity}")
                    if similarity > threshold:
                        similar_leaves.append({"class": class_name, "filename": filename, "similarity": similarity})
                except Exception as e:
                    print(f"Error calculando la similitud: {str(e)}")

    return similar_leaves





    



    
