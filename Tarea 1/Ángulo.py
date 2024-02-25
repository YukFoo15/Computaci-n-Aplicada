import os
import math


os.system("clear")

print("Cálculo del tercer ángulo de un triángulo \n")
ang1= int(input("Introduzca el valor del ángulo 1: "))
ang2= int(input("Introduzca el valor del ángulo 2: "))

ang3 = 180 - ang1 - ang2

print(f"\nEl valor del ángulo es: {ang3}")