"""Escribe un programa en Python que solicite al usuario ingresar su año de nacimiento, 
año actual y calcule su edad. Luego, muestre un mensaje en pantalla indicando el nombre y apellido 
de la persona y la edad calculada en pantalla. 
"""
print("")
print("**************************************")
name=input("por Favor Digite Su Nombre: ")
Apellido=input("Por Favor Digite Su Apellido: ")
Año_nacimiento=int(input("Por favor Digite Su año de Nacimiento: "))
Año_actual=2025
edad_actual=(Año_actual-Año_nacimiento)
print(f"Hola señor {name} {Apellido} su edad calculada es {edad_actual }")
print("")
print("**************************************")




