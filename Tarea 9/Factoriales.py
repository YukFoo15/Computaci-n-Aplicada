def leer_arreglo():
    arreglo = []
    n = int(input("Ingrese la cantidad de números en el arreglo: "))
    for i in range(n):
        num = int(input(f"Ingrese el número {i + 1}: "))
        arreglo.append(num)
    return arreglo

def factorial(numero):
    if numero == 0:
        return 1
    fact = 1
    for i in range(1, numero + 1):
        fact *= i
    return fact

def calcular_factoriales_lista(lista):
    factoriales = []
    for numero in lista:
        fact = factorial(numero)
        factoriales.append(fact)
    return factoriales

if __name__ == "__main__":
    arreglo = leer_arreglo()
    factoriales = calcular_factoriales_lista(arreglo)

    print("Lista original:", arreglo)
    print("Factoriales de los números:", factoriales)