import os


while(True):
    os.system("clear")

    print("Impresión de tablas de multiplicar hasta un límite introducido por el usuario: \n")
    tab = int(input("Ingrese el número de la tabla que desea imprimir: "))
    mult = int(input("Ingrese el múltiplo límite para la tabla: "))
    t = 1

    for i in range(1, mult+1):
        print(f"{tab} x {i} = {tab*i}")


    res = input("¿Desea continuar? (S/N)")
    if res.upper() == "N": break