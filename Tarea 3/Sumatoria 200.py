import os

while True:
    os.system("clear")
    print("Impresión de una sumatoria interrumpida al ser igual o mayor a 200: \n")
    sumatoria = 0
    lim = 0

    while sumatoria < 200:
        num = float(input("Ingrese un número (ingrese 0 para terminar): "))
        if num == 0:
            break
        sumatoria += num
        lim += 1

    if lim == 0:
        print("No se ingresaron números.")
    else:
        print(f"Se ingresaron {lim} números.")
        print(f"La suma total de los números es: {sumatoria}")

    res = input("¿Desea continuar? (S/N): ")
    if res.upper() == "N":
        break


