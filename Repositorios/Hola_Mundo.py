print("hola mundo")

message1="hola mundo"
message2="Adios mundo"

print(message2.upper())

nombre="Atanacio"
apellido="Ramírez"

print(nombre + " " + apellido) #concatenacion de textos

nombre_comleto=f"{nombre} {apellido}" # concatenacion de textos

print(nombre_comleto)

#Limpiar cadena (espacios al inicio o final)

mensaje="     hola     "
print(mensaje.strip()) #elimina espacios inicio y final
print(mensaje.lstrip()) # elimina espacios al inicio

texto="no\ndos\ntres"# el operador \n salta el texto a la línea siguiente
print(texto)