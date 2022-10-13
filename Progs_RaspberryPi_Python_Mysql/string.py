nombre = "Laura Balandran"
texto = "Texto del RFID"
rfid = 8462534552

#ESTE PROGRAMA REALIZA UNA PRUEBA DEL QUERY QUE DESEO REALIZAR PARA REVISAR QUE ESTA ESCRITO CORRECTAMENTE
# "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Laura Balandran','Test Python 4',8462534552);"
query = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('" + nombre + "','" + texto + "'," + str(rfid) + ")"

print (query)
