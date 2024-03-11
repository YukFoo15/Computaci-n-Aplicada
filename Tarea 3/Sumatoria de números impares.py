import os

while True:
    os.system("clear")

    print("Impresión ascendente de números impares: \n")
    lim = int(input("Ingrese el múltiplo límite para la sucesión: "))
    sumatoria = 0
    n = 1

    while n <= lim:
        sumatoria += n
        n += 2 

    print(f"La suma de los números impares hasta el número {lim} es: {sumatoria}\n")
    res = input("¿Desea continuar? (S/N)")
    if res.upper() == "N":
        break