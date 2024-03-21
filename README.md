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
La aplicación cuenta con las siguientes funciones:

- home: Página principal.
- cámara: Página de la cámara solo para desktop .
- predicción: Página de predicción para subir imágenes o tomar fotos.
- Búsqueda: Página de búsqueda de plantas en la base de datos


## Swagger
Swagger se encuentra [http://localhost/api/docs](http://localhost/api/docs)
