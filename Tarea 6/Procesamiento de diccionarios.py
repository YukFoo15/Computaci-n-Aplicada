import os
os.system("clear")

nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

trabajadores = {}

for i in range(len(nombres)):
    trabajadores[nombres[i]] = sueldos[i]

print("El diccionario de trabajadores es:", trabajadores)

print("Impresión de las llaves:")
for nombre in trabajadores.keys():
    print(nombre)

print("Impresión de los valores:")
for sueldo in trabajadores.values():
    print(sueldo)

print("Impresión de llave y valor:")
for nombre, sueldo in trabajadores.items():
    print(nombre, "-", sueldo)

suma_sueldos = sum(trabajadores.values())
print("La suma de los sueldos es:", suma_sueldos)

promedio_sueldos = suma_sueldos / len(trabajadores)
print("El promedio de los sueldos es:", promedio_sueldos)
