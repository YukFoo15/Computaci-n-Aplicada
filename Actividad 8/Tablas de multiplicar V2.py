import os


while(True):
    os.system("clear")

    print("Impresión de tablas de multiplicar: \n")
    tab = int(input("Ingrese hasta qué tabla desea imprimir: "))
    mult = int(input("Ingrese el múltiplo límite para cada tabla:\n "))
   

    for i in range(1, tab+1):
        print(f"\nTabla del {i}.")
        
        for j in range(1, mult+1):
            print(f"{i} x {j} = {tab*j}")

    res = input("¿Desea continuar? (S/N)")
    if res.upper() == "N": break