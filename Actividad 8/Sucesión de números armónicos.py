import os
import math 
os.system("clear")

print("Impresión de sucesión de números arm+onicos con su suma: \n")
lim = int(input("Introduzca el límite de la sucesión: "))
print(f"Imprimiendo números armónicos del 1 al {lim}: ")

sumatoria = 0
for i in range(1, lim + 1):
    n = 1 / math.factorial(i)
    print(n, end=" ")
    sumatoria = sumatoria + n

print("\nLa suma de los números armónicos es:", sumatoria)