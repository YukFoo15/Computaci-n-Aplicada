import os; os.system("clear")

print("Verificación de la suma de dos números y un tercero \n")



print("Introduzca tres números enteros, separados por <Enter>:")

n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3:
    print("Son iguales")
else:
    print("Son distintos")

print("Proceso terminado")