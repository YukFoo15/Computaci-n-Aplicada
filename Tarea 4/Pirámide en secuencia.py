import os
os.system("clear")

print("Impresión de una pirámide hecha con la secuencia de números deseada: \n")
n = int(input("Ingrese el número límite de la secuencia: "))
NUMEROS = []

for i in range(1, n + 1):
    NUMEROS.append(i)
    print(*NUMEROS)
