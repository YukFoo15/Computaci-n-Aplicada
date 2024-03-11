import os

while True:
    os.system("clear")
    print("Cálculo del número mayor en una serie de números determinada por el usuario: \n")
    maximo = None

    while True:
        num = float(input("Ingrese un número (ingrese 0 para terminar): "))
        if num == 0:
            break
        if maximo is None or num > maximo:
            maximo = num

    if maximo is None:
        print("No se ingresaron números.")
    else:
        print(f"El número máximo ingresado es: {maximo}")

    res = input("¿Desea continuar? (S/N): ")
    if res.upper() == "N":
        break
