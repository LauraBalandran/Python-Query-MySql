#Bibliotecas
import mysql.connector

#Programa
print ("Conectando a la base de datos...")
cnx = mysql.connector.connect(user='rociolan', password='1234', host='192.168.1.156', database='codigoIoT')
print ("Conexión realizada")
print(cnx)

print("Cerrar conexión")
cnx.close()
print("Conexión cerrada")

