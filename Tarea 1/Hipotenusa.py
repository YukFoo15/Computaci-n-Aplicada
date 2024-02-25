import os
import math


os.system("clear")

print("Cálculo de la hipotenusa de un triángulo rectángulo \n")
lado1= int(input("Introduzca la longitud del lado 1: "))
lado2= int(input("Introduzca la longitud del lado 2: "))

hip = math.sqrt(lado1 * lado1 + lado2 * lado2)

print(f"\nEl valor de la hipotenusa es {hip}")