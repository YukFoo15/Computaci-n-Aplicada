import os; os.system("clear")

print("Verificación de número mayor \n")

print("Introduzca tres números enteros, separados por <Espacio>: ")

n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 > 1 and n1 > n3:
    print(f" {n1} es mayor que, {n2} y {n3}")

elif n2 > n1 and n2 > n3:
    print(f" {n2} es mayor que, {n1} y {n3}")
else: 
    print(f" {n3} es mayor que, {n1} y {n2}")

print("\nProceso terminado")