# Docker Setup for FlaskDeppLeaves

## Building and Running the Application with Docker

Para ejecutar la aplicación usando Docker, sigue estos pasos:

1. Abre una terminal en el directorio del proyecto.
2. Ejecuta el siguiente comando para construir y ejecutar la aplicación:

    ```bash
    docker-compose up
    ```

    

3. La aplicación estará disponible en [http://127.0.0.1:5000](http://127.0.0.1:5000/).

## Detener la Aplicación Docker

Para detener la aplicación Docker, utiliza el siguiente comando:

```bash
docker-compose down
```
Este comando detendrá y eliminará los contenedores de la aplicación.

## Revisar Problemas y Registros
Si encuentras algún problema o deseas revisar los registros de la aplicación, puedes utilizar el siguiente comando:

```bash
docker-compose logs

```
Esto te proporcionará información detallada sobre los registros de la aplicación y te ayudará a identificar cualquier problema que pueda haber ocurrido.
