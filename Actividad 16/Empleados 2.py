import os

class Empleado:
    def __init__(self, nombre, edad, sexo, casado, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.casado = casado
        self.sueldo = sueldo

    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Sexo: {"Mujer" if self.sexo=="M" else "Hombre"} - Casado: {"Casado(a)" if self.casado else "Soltero(a)"} - Sueldo: {self.sueldo} \n"
    


os.system("clear")
empleado1 = Empleado("José Díaz", 35, "H", False, 1200 )
print("Nombre: ", empleado1.nombre)
print("Sexo: ", empleado1.sexo)
print("Casado: ", empleado1.casado)
print("Sueldo: ", empleado1.sueldo)
print(empleado1)

empleado2 = Empleado("María López", 40, "M", True, 1400)
print(empleado2)

empleado3 = Empleado("Rocío Soto", 45, "M", False, 2000)
print(empleado3)

print(f"Total de sueldos de los tres empleados ingresados: ", (empleado1.edad + empleado2.edad + empleado3.edad))