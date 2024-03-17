import os; os.system("clear")

print("Impresión del factorial de n números enteros.\n")

n = int(input("Ingrese la cantidad de números a los que desea obtener el factorial: "))


for i in range (1, n+1):
    print(f"{i}! = ", end="")
    f = 1
    for j in range (1, i+1):
        f = f * j
    print(f"{f}")

