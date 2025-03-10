"""Diseña un programa que dado el precio de venta de un artículo calcule su precio antes de impuestos.
 IVA (25%)
"""
print("")
print("***************************\n******************** ")
precio_venta=int(input("Por Digite el Precio de Venta del Articulo: "))
iva=int(input("Digite el valor del IVA: "))
precio_sin_IVA=(precio_venta/((100+iva)/100))
print(f"el precio sin IVA es de: {precio_sin_IVA}")
print("Verificando el precio a pagar es: ", ((precio_sin_IVA)*(1+(iva/100))))
print("")
print("***************************\n******************** ")
