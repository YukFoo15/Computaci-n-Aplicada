import os

def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

def metros_a_pies(metros):
    return metros * 3.281

def mostrar_menu():
    os.system("clear")
    print("1. Convertir pulgadas a centímetros")
    print("2. Convertir metros a pies")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pulgadas = float(input("Ingrese la longitud en pulgadas: "))
            centimetros = pulgadas_a_centimetros(pulgadas)
            print(f"{pulgadas} pulgadas son {centimetros} centímetros.")
        elif opcion == "2":
            metros = float(input("Ingrese la longitud en metros: "))
            pies = metros_a_pies(metros)
            print(f"{metros} metros son {pies} pies.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            input("Opción no válida. Presione Enter para continuar.")

if __name__ == "__main__":
    main()