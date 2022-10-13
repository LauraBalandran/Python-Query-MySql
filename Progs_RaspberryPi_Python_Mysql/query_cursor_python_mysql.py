#Bibliotecas
import mysql.connector

#Conexión
print ("Conectando a la base de datos...")
cnx = mysql.connector.connect(user='rociolan', password='1234', host='127.0.0.1', database='codigoIoT')

#cursor
cursor = cnx.cursor()

#Query
query = ("SELECT * FROM rfid where id=10';")

#Ejecución del cursor
cursor.execute(query)

res= cursor.fetchall()

for x in res:
    print (x)

#Cerrar conexión
cursor.close()
cnx.close()
print("Conexión cerrada")

