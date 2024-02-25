import os
import math


os.system("clear")

print("Conversor de temperatura Celsius a Farenheit \n")
cel= int(input("Introduzca la temperatura en grados Celsius: "))

res = (cel * 9/5) + 32

print(f"\nLa temperatura en grados Farenheit es: {res}")