import os; os.system("clear")

lista1 = []
lista2 = []
lista3 = []

print("Multiplicación de dos listas de números con 5 términos \n")

print(f"\nIngrese los 5 términos de la lista 1: ")
for i in range (5):
    n = int(input(f"Lista 1[{i+1}] =  "))
    lista1.append(n) 
print(f"\nLista 1: {lista1}")

print(f"\nIngrese los 5 términos de la lista 2: ")
for i in range (5):
    n = int(input(f"Lista 2[{i+1}] =  "))
    lista2.append(n) 
print(f"\nLista 2: {lista2}")


print("\nCalculando la suma de las listas ")
for i in range (5):
    lista3.append(lista1[i] * lista2[i])  


print(f"\nLa lista con la multiplicación es: {lista3}")