import os
os.system("clear")

cad = input("Ingrese una cadena: ")

apariciones = {}

for car in cad:
    if car in apariciones:
        apariciones[car] += 1
    else:
        apariciones[car] = 1

print("El diccionario de apariciones de caracteres es:", apariciones)
