#Bibliotecas
import mysql.connector

#Conexión
print ("Conectando a la base de datos...")
cnx = mysql.connector.connect(user='rociobc', password='1234', host='127.0.0.1', database='codigoIoT')
#cursor = cnx.cursor()

#Query
query = ("SELECT id,nombre,temp,humedad FROM clima WHERE id=12;")

#Ejecución
#cursor.execute(query)
res= cnx.cmd_query(query)


#Imprimir resultado
print("Respuesta")
#print(cursor)
print(res)

#Cerrar conexión
#cursor.close()
cnx.close()
print("Conexión cerrada")

