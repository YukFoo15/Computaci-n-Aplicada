import os
os.system("clear")

print("Impresión de sucesión de números pares con su suma: \n")
lim = int(input("Introduzca el límite de la sucesión: "))
print(f"Imprimiendo números pares del 1 al {lim}: ")

sumatoria = 0
for i in range(1, lim + 1):
    if i % 2 == 0:
        print(i, end=" ")
        sumatoria = sumatoria + i

print("\nLa suma de los números pares es:", sumatoria)

