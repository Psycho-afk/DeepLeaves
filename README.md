# FlaskDeppLeaves

FlaskDeppLeaves es un proyecto que utiliza la arquitectura de red neuronal profunda ResNet50, desarrollada por Kaiming He, Xiangyu Zhang, Shaoqing Ren y Jian Sun. Además, incorpora modelos como MobilenetV1 y MobilenetV2.

La aplicación web tiene como objetivo destacar la diversidad de flora en la Universidad San Buenaventura.

## Docker

Para ejecutar la aplicación utilizando Docker, sigue las instrucciones en el documento README.Docker.md.

## Ejecución desde la máquina local

Antes de ejecutar la aplicación localmente, asegúrate de tener instalados los requisitos que se encuentran en el directorio `/app`. Puedes instalarlos utilizando el siguiente comando:

```bash
pip install -r app/requirements.txt
```
Luego, ejecuta la aplicación con:

```bash
python wsgi.py
```
## Funcionalidades
La aplicación cuenta con las siguientes rutas:

- /index: Página de inicio.
- /home: Página principal.
- /camara: Página de la cámara.
- /infoPl: Página de información de plantas.
- /: Página "about".
- /red: Página de la red neuronal.

Además, ofrece rutas para predecir hojas a partir de imágenes y capturar fotos para realizar predicciones.

## MongoDB

Para poner en marcha la base de datos de este proyecto en docker, sigue los pasos descritos a continuación:

1. Acceso al Contenedor de MongoDB
Primero, debes acceder al contenedor de MongoDB. Utiliza el siguiente comando para abrir una terminal dentro del contenedor:

```bash
docker exec -it mongdb /bin/sh
```
2. Copia del Archivo de la Base de Datos
A continuación, necesitas copiar el archivo de la base de datos desde tu máquina local al contenedor de MongoDB. Para ello, ejecuta el siguiente comando, reemplazando "Ruta relativa donde se encuentra la bd" por la ruta correcta en tu sistema:

```bash
docker cp "Ruta relativa donde se encuentra la bd dentro de la maquina"/database_pl.js mongodb:/database_pl.js
```

3. Ejecución del Script de la Base de Datos
Una vez que el archivo database_pl.js esté dentro del contenedor, puedes ejecutar el script dentro de la base de datos de mongo para levantar la base de datos. Desde la terminal dentro del contenedor de MongoDB, corre el siguiente comando:

```bash
load("/database_pl.js");
```



## Swagger
Swagger se encuentra [http://localhost/api/docs](http://localhost/api/docs)