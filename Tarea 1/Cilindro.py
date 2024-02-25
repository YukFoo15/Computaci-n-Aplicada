import os
import math

print("Calculadora de volumen de un cilindro\n")

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

volumen = math.pi * radio ** 2 * altura

print(f"\nEl volumen del cilindro con radio {radio} y altura {altura} es: {volumen}")
