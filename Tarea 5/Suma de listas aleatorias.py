import random
import os; os.system("clear")

n = 10
lista1 = []
lista2 = []
lista3 = []
suma = 0

print("\nGeneración de listas con números aleatorios ")

for i in range (n):
    lista1.append(random.randint(1,10))
    lista2.append(random.randint(1,10))

    if lista1[i]%2 != 0 and lista2[i]%2 != 0:
        suma = lista1[i] + lista2[i]
        lista3.append(suma)

print(f"\nLista 1: {lista1} \nLista 2: {lista2} \nLista 2: {lista3} \n")