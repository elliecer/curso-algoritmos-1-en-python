"""Calcula la longitud de la circunferencia y el área del circulo dado el radio.
Profe Ellicer
"""

import os                    # Importo libreria os
def limpiar_terminal():          # creo la funcion Limpiar_terminal
    os.system("cls")              # Ejecuta el comando CLS
    
limpiar_terminal()              # llamo la función Creada
Area=0
Radio=0
print("*********************************************************\n*********************************************************")
print("*********************************************************\n*********************************************************")
print("")
from cmath import  pi
Radio=float(input("Digite el valor del radio de la circuferencia en cm: "))
Area=(pi*Radio**2)
print(f"el Area calculada es de:{Area} cm^2")
print("")
print("*********************************************************\n*********************************************************")
print("*********************************************************\n*********************************************************")


