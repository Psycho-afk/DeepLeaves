import mysql.connector
import time

# MSQL
max_retries = 10
retry_delay = 3  # segundos

def conectar_mysql():
    for i in range(max_retries):
        try:
            connection = mysql.connector.connect(
                user='root', password='root', host='mysql', port="3306", database='db')
            print("Conexión a MySQL exitosa")
            return connection
        except mysql.connector.Error as e:
            print(f"Error de conexión a MySQL: {e}")
            print(f"Reintentando en {retry_delay} segundos...")
            time.sleep(retry_delay)
    print("No se pudo conectar a MySQL después de varios intentos")

# Llama a la función conectar_mysql para establecer la conexión
#connection = conectar_mysql() # Ejemplo para conector


def buscar_plantas(termino_busqueda):
    # Conecta a la base de datos
    connection = conectar_mysql()
    cursor = connection.cursor(dictionary=True)

    # Realiza la búsqueda de plantas por nombre
    query = "SELECT * FROM plantas WHERE nombre LIKE %s"
    cursor.execute(query, (f"%{termino_busqueda}%",))

    # Obtiene los resultados de la búsqueda
    resultados = cursor.fetchall()

    # Cierra la conexión a la base de datos
    cursor.close()
    connection.close()

    return resultados
