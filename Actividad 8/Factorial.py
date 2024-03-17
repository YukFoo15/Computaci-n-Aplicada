import os; os.system("clear")

print("Impresión del factorial de un número ingresado por el usuario.\n")

n = int(input("Ingrese el número al que se le realizará el cálculo: "))

f = 1
for i in range (1, n+1):
    f = f * i

print(f"El factorial del número {n} es: {f}")