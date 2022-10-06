#Bibliotecas
import mysql.connector

#Programa
print ("Conectando a la base de datos...")
cnx = mysql.connector.connect(user='rociobc', password='1234', host='127.0.0.1', database='codigoIoT')
print ("Conexión realizada")
print(cnx)

print("Cerrar conexión")
cnx.close()
print("Conexión cerrada")

