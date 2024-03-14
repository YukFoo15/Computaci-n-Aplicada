import os

while True:
    os.system("clear")
    print("Impresión de números pares e impares de 1 a n y su suma: \n")
    n = int(input("Introduzca el límite de la sucesión: "))

    s = 0
    print("\nNúmeros pares y su suma.\n")
    for i in range (2, n+1, 2):
        print(i, end=" ")
        s = s + i
    print("\nLa suma es: ", s)

    s = 0
    print("\nNúmeros impares y su suma.\n")
    for i in range (1, n+1, 2):
        print(i, end=" ")
        s = s + i
    print("\nLa suma es: ", s)   

    res = input("¿Desea continuar? (S/N): ")
    if res.upper() == "N":
        break