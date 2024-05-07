import os
os.system("clear")

def mayores (lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] > m:
            m = lista[n]
    return m

def menores (lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] > m:
            m = lista[n]
    return m

def leer ():
    nums = []
    while True:
        d = int(input("Ingrese un número: "))
        if d == -1: break
        nums.append(d)
    return nums