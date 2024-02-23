# Programa que calcula el área de un círculo de radio determinado por el usuario.
import math
radio=float(input("Introduzca el radio del círculo:"))
pi = math.pi
area = pi * (radio * radio)
print("El área del círculo es:", area)