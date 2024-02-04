
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

 #Ruta de la imagen que quieres predecir
image_path = r'F:\Universidad\Imagenes nuevas plantas PDG\Naranjo comun\IMG_6373.JPG'

# Cargar la imagen y aplicar transformaciones necesarias
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Ajusta el tamaño de la imagen según lo que el modelo espera
    transforms.ToTensor(),           # Convierte la imagen a un tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normaliza la imagen
])

image = Image.open(image_path)
input_image = transform(image)
input_batch = input_image.unsqueeze(0)  # Agrega una dimensión extra para el lote

#Clase para cargar el modelo de pytorch
# Carga modelo

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class InvertedResidual(nn.Module):
    def __init__(self, in_channels, out_channels, stride, expand_ratio=6):
        super(InvertedResidual, self).__init__()
        hidden_dim = round(in_channels * expand_ratio)
        self.use_res_connect = stride == 1 and in_channels == out_channels

        layers = []
        if expand_ratio != 1:
            layers.append(nn.Conv2d(in_channels, hidden_dim, kernel_size=1, bias=False))
            layers.append(nn.BatchNorm2d(hidden_dim))
            layers.append(nn.ReLU6(inplace=True))
        
        layers.extend([
            nn.Conv2d(hidden_dim, hidden_dim, kernel_size=3, stride=stride, padding=1, groups=hidden_dim, bias=False),
            nn.BatchNorm2d(hidden_dim),
            nn.ReLU6(inplace=True),
            nn.Conv2d(hidden_dim, out_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(out_channels),
        ])

        self.conv = nn.Sequential(*layers)

    def forward(self, x):
        if self.use_res_connect:
            return x + self.conv(x)
        else:
            return self.conv(x)

class MobileNetV2(nn.Module):
    def __init__(self, num_classes=5, width_multiplier=1.0):
        super(MobileNetV2, self).__init__()
        # Inicializar el ancho de la red según el multiplicador de ancho
        input_channel = int(32 * width_multiplier)
        last_channel = int(1280 * width_multiplier)

        # Etapas de MobileNetV2
        features = [
            nn.Conv2d(3, input_channel, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(input_channel),
            nn.ReLU6(inplace=True),
        ]

        inverted_residual_setting = [
            # t, c, n, s (expansion factor, output channels, number of blocks, stride)
            [1, 16, 1, 1],
            [6, 24, 2, 2],
            [6, 32, 3, 2],
            [6, 64, 4, 2],
            [6, 96, 3, 1],
            [6, 160, 3, 2],
            [6, 320, 1, 1],
        ]

        for t, c, n, s in inverted_residual_setting:
            output_channel = int(c * width_multiplier)
            for i in range(n):
                stride = s if i == 0 else 1
                features.append(InvertedResidual(input_channel, output_channel, stride, expand_ratio=t))
                input_channel = output_channel

        features.append(nn.Conv2d(input_channel, last_channel, kernel_size=1, bias=False))
        features.append(nn.BatchNorm2d(last_channel))
        features.append(nn.ReLU6(inplace=True))

        self.features = nn.Sequential(*features)

        # Capa de clasificación
        self.classifier = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(last_channel, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = F.adaptive_avg_pool2d(x, (1, 1))
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x
    
ruta_absoluta = 'F:/Universidad/ProyectoDeepleaves/ModeloPytorch/modelo_entrenado_mobilenetv2.pth'
    # Cargar el modelo

    # Cargar los pesos previamente guardados
modelo = torch.load(ruta_absoluta,map_location=torch.device('cpu'))
modelo = modelo.to(device)
modelo.eval()

# Realizar la predicción
with torch.no_grad():
    output = modelo(input_batch)



# Obtener las probabilidades predichas y la clase predicha
probabilidades = torch.nn.functional.softmax(output[0], dim=0)
clase_predicha = torch.argmax(probabilidades).item()

# Imprimir las probabilidades para cada clase
print("Probabilidades:")
for i, prob in enumerate(probabilidades):
    print(f"Clase {i}: {prob.item()}")

# Imprimir la clase predicha
print(f"Clase predicha: {clase_predicha}")