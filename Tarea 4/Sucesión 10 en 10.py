import os
os.system("clear")

print("Impresión de sucesión numérica con incremento de 10: \n")
lim = int(input("Introduzca el límite de la sucesión: "))

print(f"Imprimiendo números del 1 al {lim} de 10 en 10: ")

for i in range(1, lim + 1, 10):
    print(i, end=" ")

