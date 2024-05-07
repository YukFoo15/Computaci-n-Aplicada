import os

def pi (lista):
    lp = []
    li = []
    for n in lista:
        if n  % 2 == 0:
            lp.append(n)
        else:
            li.append(n)
    return lp, li

os.system("clear")

nums = [9,8,7.5,6,9.5,7,10,6,7]
lp, li = pi(nums)

print(f"Lista de los {len(nums)} números obtenidos: {nums}")
print(f"Lista de los {len(lp)} números pares obtenidos: {lp}")
print(f"Lista de los {len(li)} números impares obtenidos: {li}")