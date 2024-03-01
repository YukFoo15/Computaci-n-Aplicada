import os; os.system("clear")

print("Verificación de la suma de dos números y un tercero \n")

print("Introduzca tres números enteros, separados por <Espacio>: ")

n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + n2 == n3:
    print(f"Caso 1 : {n1} + {n2} = {n3}")

elif n1 + n3 == n2:
    print(f"Caso 2 : {n1} + {n3} = {n2}")

elif n2 + n3 == n1:
    print(f"Caso 3 : {n2} + {n3} = {n1}")

elif n2 == n3 == n1:
    print(f"Caso 4 : {n2} = {n3} = {n1}")

else: 
    print("Caso 5 : Los números son diferentes y no suman")

print("\nProceso terminado")