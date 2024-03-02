import os; os.system("clear")

print("Convertidor a números romanos\n")

print("Introduzca un número del 1 al 10 para asignarle su equivalente en numeración romana: ")

n = int(input())

if n == 1:
    print(f"El número {n} es igual a I. ", end="")
elif n == 2:
    print(f"El número {n} es igual a II. ", end="")
elif n == 3:
    print(f"El número {n} es igual a III. ", end="")
elif n == 4:
    print(f"El número {n} es igual a IV. ", end="")
elif n == 5:
    print(f"El número {n} es igual a V. ", end="")
elif n == 6:
    print(f"El número {n} es igual a VI. ", end="")
elif n == 7:
    print(f"El número {n} es igual a VII. ", end="")
elif n == 8:
    print(f"El número {n} es igual a VIII. ", end="")
elif n == 9:
    print(f"El número {n} es igual a IX. ", end="")
elif n == 10:
    print(f"El número {n} es igual a X. ", end="")
else:
    print("\nEl número no se encuentra dentro del rango")


print("\nProceso terminado")