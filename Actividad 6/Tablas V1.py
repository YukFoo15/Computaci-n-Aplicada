import os


while(True):
    os.system("clear")

    print("Impresión de tablas de multiplicar: \n")
    tab = int(input("Ingrese la tabla deseada: "))
    mult = int(input("Ingrese el múltiplo límite: "))
    c = 1

    while c <= mult:
        print(f"{tab} x {c} = {tab*c}")
        c += 1

    res = input("¿Desea continuar? (S/N)")
    if res.upper() == "N": break

print("\nProceso terminado")