import os


while(True):
    os.system("clear")
    tc = 17.00

    print("Tabla de conversión de divisas para conversión de peso a dolar: \n")
    vi = float(input("Valor inicial: "))
    vf = float(input("Valor final: "))

    c = vi
    print("\nPeso\tDolar")
    print("-"*15)
    while c <= vf:
        print(f"{c}\t{c/tc:.2f}")
        c = c + 1
        print("-"*15)

    val = input("¿Desea continuar (S/N)? ")
    if val.upper() == "N": break

print("\nProceso terminado")