import os
os.system("clear")

def pares (lista):
    p = []
    for n in lista:
        if n % 2 == 0:
            p.append(n)
    return p

nums = [1,2,3,4,5,6,7,8,9,10]

res = pares(nums)

print(f"El total de números pares es: {len(res)} y son {res}")