# FROM python:3.10.13-slim as base

# WORKDIR /app

# # Copy the source code into the container.
# COPY . .

# RUN pip install -r requirements.txt

# EXPOSE 5000

# # Run the application. 'myenv.Lib.site-packages.werkzeug.wsgi'
# CMD flask run app gunicorn --bind=0.0.0.0:5000 wsgi:app

#-------------------------------- 

# FROM python:3.10.13-slim as base

# # Establece el directorio de trabajo
# WORKDIR /app

# # Copia los archivos necesarios al contenedor
# COPY . /app

# # Instala las dependencias
# RUN pip install -r requirements.txt

# # Expone el puerto en el que se ejecutará tu aplicación Django
# EXPOSE 5000

# # Comando para ejecutar la aplicación cuando se inicie el contenedor
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

#--------------------------------

FROM python:3.10.13-slim as base

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]