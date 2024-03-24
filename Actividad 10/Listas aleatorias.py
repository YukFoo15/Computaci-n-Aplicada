import random
import os; os.system("clear")

n = 10
lista1 = []
lista2 = []
lista3 = []

print("\nGeneración de listas con números aleatorios ")
for i in range (n):
    lista1.append(random.randint(1,10))
    lista2.append(random.randint(1,10))
    lista3.append(lista1[i] + lista2[i])

print(f"\nLista 1: {lista1} \nLista 2: {lista2} \nLista 3{lista3}")