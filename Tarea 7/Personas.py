import os
os.system("clear")

A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}
C = {"Pablo", "Mateo"}
D = {"Reynaldo", "Angelica"}

print("Unión: ")
print(f"Unión de A y B: {A.union(B)}")
print("Intersección: ")
print(f"Intersección de A y B: {A.intersection(B)}")
print("Diferencia: ")
print(f"Diferencia entre A y B: {A.difference(B)}")
print("Diferencia simétrica: ")
print(f"Diferencia simétrica entre A y B: {A.symmetric_difference(B)}")
print("Prueba de subconjuntos")
print(f"C es un subconjunto de B: {C.issubset(B)}")
print("Prueba de superconjuntos")
print(f"A es superconjunto de Reynaldo, Angelica: {A.issuperset(D)}")
print("Verificación de elementos en un conjunto: ")
print(f"Pedro se encuentra en A: {'Pedro' in A}")
print(f"Lilia no se encuentra en B: {'Lilia' not in B}")