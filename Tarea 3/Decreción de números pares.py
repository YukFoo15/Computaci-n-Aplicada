import os

while True:
    os.system("clear")

    print("Impresión descendente desde el número 100 en números pares: \n")
    lim = int(input("Ingrese el múltiplo límite para la regresión: "))
    sumatoria = 0
    n = 100

    while n >= lim:
        sumatoria += n
        n -= 2 

    print(f"La suma de los números pares desde el número 100 hasta el número {lim} es: {sumatoria}\n")
    res = input("¿Desea continuar? (S/N)")
    if res.upper() == "N":
        break
