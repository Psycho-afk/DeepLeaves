import pymongo
import time

# MSQL
max_retries = 10
retry_delay = 3  # segundos

def conectar_mongo():
    for i in range(max_retries):
        try:
            client = pymongo.MongoClient("mongodb://mongodb:27017/")
            db = client["bd_plantas"]  # Reemplaza "nombre_de_tu_base_de_datos" con el nombre de tu base de datos
            print("Conexión a MongoDB exitosa")
            return db
        except pymongo.errors.ConnectionFailure as e:
            print(f"Error de conexión a MongoDB: {e}")
            print(f"Reintentando en {retry_delay} segundos...")
            time.sleep(retry_delay)
    print("No se pudo conectar a MongoDB después de varios intentos")



def buscar_plantas(termino_busqueda):
    db = conectar_mongo()
    plantas = db["plantas"]
    resultados = plantas.find({"nombre": {"$regex": termino_busqueda, "$options": "i"}})
    return list(resultados)   




