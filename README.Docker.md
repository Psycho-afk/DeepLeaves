### Building and running your application

Ejecuta la aplicación de la sigueinte manera:
`docker-compose up -d --build --scale app=1`.

Donde app=1 es el numero de usuarios en la aplicación 
La aplicación esta en  http://localhost.

para detener:
`docker-compose down`

revisar problemas:
`docker-compose logs`

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)