import os

os.system("clear")


print("Promedio de tres calificaciones \n")
print("Introduzca 3 calificaciones separadas por espacio (Pueden tener decimales)") 

c1, c2, c3 = input().split()
c1, c2, c3 = float(c1), float(c2), float(c3)

prom = ((c1+c2+c3)/3)

print(f"El promedio de {c1}, {c2} y {c3} es {prom:.2f}")