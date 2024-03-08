import os


while(True):
    os.system("clear")

    print("Impresión de la conjetura de Collatz: \n")
    num = int(input("Ingrese un número entero positivo: "))

    while num != 1:
        print(num, end=" ")
        if num % 2 == 0:
            num //= 2
        else: 
            num = num * 3 + 1

    print(num)

    res = input("¿Desea continuar (S/N)? ")
    if res.upper()=="N": break

print("\nProceso terminado")