import os; os.system("clear")

print("Verificación de tres números consecutivos \n")

print("Introduzca tres números enteros, separados por <Espacio>: ")

n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + 1 == n2 and n2 + 1 == n3:
    print(f"Los números {n1}, {n2} y {n3} son consecutivos")

else: 
    print("Los números no son cosecutivos")

print("\nProceso terminado")