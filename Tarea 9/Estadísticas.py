def leer_arreglo():
    arreglo = []
    n = int(input("Ingrese la cantidad de números en el arreglo: "))
    for i in range(n):
        num = int(input(f"Ingrese el número {i + 1}: "))
        arreglo.append(num)
    return arreglo

def mayor(arreglo):
    return max(arreglo)

def menor(arreglo):
    return min(arreglo)

def media(arreglo):
    return sum(arreglo) / len(arreglo)

def varianza(arreglo):
    mu = media(arreglo)
    return sum((x - mu) ** 2 for x in arreglo) / len(arreglo)

def desviacion_estandar(arreglo):
    return varianza(arreglo) ** 0.5

if __name__ == "__main__":
    arreglo = leer_arreglo()

    print("Mayor:", mayor(arreglo))
    print("Menor:", menor(arreglo))
    print("Media:", media(arreglo))
    print("Varianza:", varianza(arreglo))
    print("Desviación estándar:", desviacion_estandar(arreglo))