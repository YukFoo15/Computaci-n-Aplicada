import os
os.system("clear")

print("Obtención del número de la suerte \n")

sum = 0
n = int(input("Introduzca su año de nacimiento, debe tener 4 cifras: "))

unidades = n % 10
sum += unidades

n //= 10
decenas = n % 10
sum += decenas

n //= 10
centenas = n % 10
sum += centenas

n //= 10
millares = n % 10
sum += millares

print(f"El número de la suerte es: {sum}")
print(f"Dígitos individuales de la suma: {millares}, {centenas}, {decenas}, {unidades}")
