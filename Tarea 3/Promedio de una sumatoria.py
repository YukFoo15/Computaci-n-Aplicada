import os

while True:
    os.system("clear")
    print("Impresión del promedio de una sumatoria: \n")
    sumatoria = 0
    lim = 0

    while True:
        num = float(input("Ingrese un número (ingrese 0 para terminar): "))
        if num == 0:
            break
        sumatoria += num
        lim += 1

    if lim == 0:
        print("No se ingresaron números.")
    else:
        promedio = sumatoria / lim
        print(f"Suma total: {sumatoria}")
        print(f"Promedio: {promedio}")
        print(f"Número de elementos: {lim}")

    res = input("¿Desea continuar? (S/N): ")
    if res.upper() == "N":
        break
