import os

def leer ():
    nums = []
    while True:
        d = float(input("Ingrese un número: "))
        if d == -1: break
        nums.append(d)
    return nums

def promedio (lista):
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

def mayprom (lista, prom):
    mp = []
    for n in lista:
        if n > prom:
            mp.append(n)
    return mp


os.system("clear")
nums = leer()
prom = promedio(nums)
mp = mayprom(nums, prom)

print(f"Lista de los {len(nums)} obtenidos: {nums}")
print(f"El promedio de los números obtenidos es: {prom}")
print(f"Se obtuvieron {len(mp)} números mayores al primedio, que son: {mp}")