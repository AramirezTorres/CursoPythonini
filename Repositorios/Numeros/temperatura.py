#programa que pide valor en grados centrigrados y convierte a fahrenheit
# (0 °C × 9/5) + 32 = 32 °F

grado_celcius=input("Ingresa los grados celcius a convertir: ")
grado_celcius=float(grado_celcius)
Farenh=(grado_celcius * (9/5)) + 32 

print(f"la conversión de: {grado_celcius} grados Farhegeit a grados Centígrados es {Farenh}")