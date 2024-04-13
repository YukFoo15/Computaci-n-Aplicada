import os; os.system("clear")

grupo = [
    {"Nombre":"Carlos", "Edad":45, "Carrera":"Sistemas", "Promedio":9},
    {"Nombre":"Rocío", "Edad":35, "Carrera":"Psicología", "Promedio":10}
]

print("El grupo original está compuesto por: ", grupo)
while True:
    datos = {}
    print("Datos del estudiante:")
    nombre = input("Nombre: ")
    if nombre != "":
        datos["Nombre"] = nombre
        datos["Edad"] = int(input("Edad: "))
        datos["Carrera"] = input("Carrera: ")
        datos["Promedio"] = float(input("Promedio: "))
        grupo.append(datos)
    else:
        break

    print(f"El grupo completo es: {grupo} y cuenta con {len(grupo)} alumnos")