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

## Swagger
Swagger se encuentra [http://localhost/api/docs](http://localhost/api/docs)