import os

def suma_pares_impares(num1, num2, opcion):
    suma = 0
    if opcion == "P":
        for num in range(num1, num2 + 1):
            if num % 2 == 0:
                suma += num
    elif opcion == "I":
        for num in range(num1, num2 + 1):
            if num % 2 != 0:
                suma += num
    return suma

def mostrar_menu():
    os.system("clear")
    print("1. Sumar números pares en un rango")
    print("2. Sumar números impares en un rango")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1" or opcion == "2":
            num1 = int(input("Ingrese el primer número del rango: "))
            num2 = int(input("Ingrese el segundo número del rango: "))
            if opcion == "1":
                suma = suma_pares_impares(num1, num2, "P")
                print(f"La suma de los números pares en el rango es: {suma}")
            else:
                suma = suma_pares_impares(num1, num2, "I")
                print(f"La suma de los números impares en el rango es: {suma}")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            input("Opción no válida. Presione Enter para continuar.")

if __name__ == "__main__":
    main()