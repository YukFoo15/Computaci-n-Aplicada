import os

while True:
    os.system("clear")
    print("Impresión de sucesiones incrementales (1 a n) o decrementales(n a 1): \n")
    print("[ 1 ] Incremental de 1 a n \n")
    print("[ 2 ] Decremental de n a 1 \n")
    print("[ 3 ] Salir \n")

    op = int(input("Elija la opción deseada: "))

    if op == 1:
        n = int(input("Introduzca el límite de la sucesión: "))
        for i in range (1, n+1):
            print(i, end=" ")

    elif op == 2:
        n = int(input("Introduzca el límite de la sucesión: "))
        for i in range (n, 0, -1):
            print(i, end=" ")

    elif op == 3:
        print("Ha elegido la opción salir. ")
        break

    else:
        print("Opción incorrecta")

print("\nPrograma terminado, gracias por utilizar la impresora de sucesiones.")