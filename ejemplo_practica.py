"""
Hola Buenos dias, calcula el area de un circulo
"""
#Entradas
radio=float(input("Por favor ingrese el radio r (m): "))
from cmath import pi
print("")
#proceso
Area=pi*(radio)**2
print("")
#salida
print(f"el area es: ({pi})*({radio})^2 = {Area} m^2")
print("")
print("")