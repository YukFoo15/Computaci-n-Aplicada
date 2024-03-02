import os; os.system("clear")

print("Verificación de días de la semana \n")

print("Introduzca un número del 1 al 7 para asignarle un día de la semana: ")

n = int(input())

if n == 1:
    print(f"El número {n} corresponde al día domingo. ", end="")
elif n == 2:
    print(f"El número {n} corresponde al día lunes. ", end="")
elif n == 3:
    print(f"El número {n} corresponde al día martes. ", end="")
elif n == 4:
    print(f"El número {n} corresponde al día miécoles. ", end="")
elif n == 5:
    print(f"El número {n} corresponde al día jueves. ", end="")
elif n == 6:
    print(f"El número {n} corresponde al día viernes. ", end="")
elif n == 7:
    print(f"El número {n} corresponde al día sábado. ", end="")
else:
    print("\nEl número no se encuentra dentro del rango")


print("\nProceso terminado")