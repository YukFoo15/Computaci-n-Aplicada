def leer_arreglo():
    arreglo = []
    n = int(input("Ingrese la cantidad de números en el arreglo: "))
    for i in range(n):
        num = int(input(f"Ingrese el número {i + 1}: "))
        arreglo.append(num)
    return arreglo

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

def sumar_digitos_lista(lista):
    sumas = []
    for numero in lista:
        suma = suma_digitos(numero)
        sumas.append(suma)
    return sumas

if __name__ == "__main__":
    arreglo = leer_arreglo()
    sumas_digitos = sumar_digitos_lista(arreglo)

    print("Lista original:", arreglo)
    print("Sumas de dígitos:", sumas_digitos)
