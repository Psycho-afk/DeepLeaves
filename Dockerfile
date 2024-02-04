# Usa una imagen base de Python 3.8
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido actual al contenedor en /app
COPY . .

# Expone el puerto 5000 (o el que estés utilizando)
EXPOSE 5001

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "app.py"]
