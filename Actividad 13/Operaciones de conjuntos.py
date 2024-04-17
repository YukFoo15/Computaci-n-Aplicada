import os
os.system("clear")
c1 = {1,2,3,4,5}
c2 = {5,6,7,8,9,10}
c3 = {9,10,11,12,13}
c4 = {3,4,5}

print("Unión: ")
print(f"Unión de c1 y c2: {c1.union(c2)}")
print(f"Unión de c1 y c3: {c1|c3}")
print("Intersección: ")
print(f"Intersección de c1 y c2: {c1.intersection(c2)}")
print(f"Intersección de c2 y c3: {c2 & c3}")
print("Diferencia: ")
print(f"Diferencia entre c1 y c4: {c1.difference(c4)}")
print(f"Diferencia entre c2 y c3: {c2 - c3}")
print("Diferencia simétrica: ")
print(f"Diferencia simétrica entre c1 y c2 {c1.symmetric_difference(c2)}")
print(f"Diferencia simétrica entre c2 y c3: {c2 ^ c3}")
print("Prueba de subconjuntos")
print(f"c4 es un subconjunto de c1: {c4.issubset(c1)}")
print(f"c2 es subconjunto de c2 {c2 >= c3}")
print("Prueba de superconjuntos")
print(f"c1 es superconjunto de c4 {c1.issuperset(c4)}")
print(f"c2 es superconjunto de c3 {c2 <= c3}")
print("Verificación de de elementos en un conjunto: ")
print(f"2 se encuentra en c1: {2 in c1}")
print(f"6 no se encuentra en c1: {6 not in c1}")