import os
os.system("clear")

n = int(input("Ingrese el número de empleados a registrar: "))
empleados = []
th = 0
tm = 0
se = 0
ss = 0

for i in range (n):
    print("Ingrese los datos del empleado/a número ", i+1)
    nombre = str(input("Nombre: "))
    edad = int(input("Edad: "))
    sexo = str(input("Sexo (h/m): ")).lower()
    sueldo = int(input("Sueldo: "))

    empleado = {"Nombre":nombre, "Edad":edad, "Sexo":sexo, "Sueldo":sueldo}
    empleados.append(empleado)

    if sexo == "h":
        th = th + 1
    elif sexo == "m":
        tm = tm +1

    se = se + edad
    ss = ss + sueldo

print("Impresión de datos de los empleados registrados: \n")
for empleado in empleados:
    print(empleado)

print("Tabla de datos de los empleados: \n")
print("Nombre\tEdad\tSexo\tSueldo")
for empleado in empleados:
    print(f"{empleado['Nombre']}\t{empleado['Edad']}\t{empleado['Sexo']}\t{empleado['Sueldo']}")

promed = se / n
promsu = ss / n

print("Resumen de datos: \n")
print("Total de empleados: ", n)
print("Total de hombres: ", th)
print("total de mujeres: ", tm)
print(f"Suma de edades: {se}, Promedio de edades: {promed}")
print(f"Suma de sueldos: {ss}, Promedio de sueldos: {promsu}")




