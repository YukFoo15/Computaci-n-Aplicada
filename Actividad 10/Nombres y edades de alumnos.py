import os; os.system("clear")

nombres = []
edades = []

print("Capturando los nombres y edades correspondientes: \n")
print("Introduzca los nombres y edades de n estudiantes, para finalizar. Presione *: \n")

while True: 
    nombre = input("Ingrese un nombre: ")
    if nombre == "*":
        break
    else:
        nombres.append(nombre)
        edad = int(input("Ingrese la edad correspondiente al nombre: "))
        edades.append(edad)

print(f"\nNombres : {nombres}. Edades: {edades}")

print("\nAlumnos mayores de edad: ")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"Nombre: {nombres[i]}. Edad: {edades[i]}")

may = max(edades)
pos = edades.index(may)
print(f"El alumno de mayor edad es: {nombres[pos]} y tiene {edades[pos]} años de edad.")
