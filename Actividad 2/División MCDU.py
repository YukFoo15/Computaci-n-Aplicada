import os
os.system("clear")

print("División de un número entero en unidades, decenas, centenas y millares \n")

n = int(input("Introduzca el número a dividir, debe tener 4 cifras: "))

unidades = n % 10
n //= 10
decenas = n % 10
n //= 10
centenas = n % 10
millar = n // 10

print(f"Millares: {millar}, Centenas: {centenas}, Decenas: {decenas}, Unidades: {unidades}")
4532