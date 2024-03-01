import os; os.system("clear")

print("Universidad Patito S.A. de C.V. \n")
print("Validación de inscripción \n")

nombre = (input("Introduzca su nombre "))
edad = int(input("Introduzca su edad "))

if edad < 18:
    print("Sólo se aceptan estudiantes mayores de edad")

else: 
    print("Introduzca dos calificaciones separadas por <Enter>: ")
    c1, c2 = int(input()), int(input())
    if c1 < 8 or c2 < 8:
        print("Sólo se aceptan estudiantes con calificaciones mayores a 8")
    else: 
        print(f"{nombre}, bienvenid@ a la Universidad Patito, su edad: {edad} años y sus calificaciones: {c1}, {c2} lo permiten ")

print("\nProceso terminado")