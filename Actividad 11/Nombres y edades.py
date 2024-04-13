import os; os.system("clear")

datos = {}

print(f"Datos: {datos, {len(datos)}}")

print("Introduzca los nombres y edades (nombre vacío para terminar): ")
while True:
    nombre = input("Introduzca un nombre: ")
    if nombre != "":
        datos[nombre] = int(input("Introduzca la edad correspondiente: "))
    else:
        break


print(f"Datos {datos}, {len(datos)}")

print(f"\n Listado de nombres y edades con suma y promedio: " )
s = p = 0

for m, c in datos.items():
    print(f"{m:<20} - {c:3}")
    s = s + c
p = s / len(datos)

print(f"La suma es: {s} y el promedio es: {p}")