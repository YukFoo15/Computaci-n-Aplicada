import os

class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} \n"
    


os.system("clear")
empleado1 = Empleado("José Díaz", 35)
print("Nombre: ", empleado1.nombre)
print("Edad: ", empleado1.edad)
empleado1.edad = 40
print(empleado1)

empleado2 = Empleado("Sandra López", 22)
print(empleado2)

empleado3 = Empleado("Lucía Ramírez", 15)
print(empleado3)

print(f"Promedio de edad de los tres empleados ingresados: ", (empleado1.edad + empleado2.edad + empleado3.edad)/3)
    