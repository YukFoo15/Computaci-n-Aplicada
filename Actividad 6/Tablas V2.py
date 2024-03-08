import os


while(True):
    os.system("clear")

    print("Impresión de tablas de multiplicar: \n")
    tab = int(input("Ingrese hasta qué tabla desea imprimir: "))
    mult = int(input("Ingrese el múltiplo límite para cada tabla: "))
    t = 1

    while t <= tab:
        print(f"\nTabla del{t}\n")
        
        c = 1
        while c <= mult:
            print(f"{tab} x {c} = {tab*c}")
            c += 1

        t += 1

    res = input("¿Desea continuar? (S/N)")
    if res.upper() == "N": break

print("\nProceso terminado")