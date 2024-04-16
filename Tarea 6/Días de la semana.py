import os
os.system("clear")

dias = {1:"Lunes", 2:"Martes", 3:"Miércoles", 4:"Jueves", 5:"Viernes", 6:"Sábado", 7:"Domingo"}

print("El diccionario de días de la semana es:", dias)

print("El primer día es:", dias[1])
print("El último día es:", dias[7])
print("El quinto día es:", dias.get(5))
print("El séptimo día es:", dias.get(7))
print("El diccionario completo es:", dias)