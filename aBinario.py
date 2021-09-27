numero=input("Por favor digita un número entre 1 y 1024: ")
numero=int(numero)
Binario=format(numero, "b")

if numero < 1025: 
    print(f"El equivalente en número Binario es: {Binario}")
else: 
    print("¡Error!: el número debe ser entre 1 y 1024")
    