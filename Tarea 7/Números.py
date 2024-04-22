import os
os.system("clear")

A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print("Unión: ")
print(f"Unión de A y B: {A.union(B)}")
print(f"Unión de B y C: {B.union(C)}")
print("Diferencia: ")
print(f"Diferencia entre A y C: {A.difference(C)}")
print("Diferencia simétrica: ")
print(f"Diferencia simétrica entre B y C: {B.symmetric_difference(C)}")
print("Intersección: ")
print(f"Intersección de B y C: {B.intersection(C)}")
print("Prueba de subconjuntos")
print(f"C es un subconjunto de B: {C.issubset(B)}")
print(f"C es un subconjunto de A: {C.issubset(A)}")
print("Verificación de elementos en un conjunto: ")
print(f"100 se encuentra en A: {100 in A}")
print(f"60 se encuentra en A, B y C: {60 in A and 60 in B and 60 in C}")
print(f"900 no se encuentra en C: {900 not in C}")