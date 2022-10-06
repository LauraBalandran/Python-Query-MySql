# Bibliotecas
import mysql.connector

# Conexión
print("Conectando a la base de datos...")
cnx = mysql.connector.connect(user='rociobc', password='1234', host='127.0.0.1', database='codigoIoT')

# Cursor
cursor = cnx.cursor()

query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Laura Balandrán','Test Python 5',89743552);"

# Ejecutar cursor
cursor.execute (query_insert)

# Realizar la operacion en Base de Datos
cnx.commit()
print ("Query Ok")

# Cerrar conexión
cursor.close()
cnx.close()
print("Conexión cerrada")