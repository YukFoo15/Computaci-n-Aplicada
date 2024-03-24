import os; os.system("clear")

lista1 = []
lista2 = []
lista3 = []

print("Suma de dos listas de números \n")
c = int(input("Ingrese el número de téminos para las listas \n"))

print(f"\nIngrese los {c} de la lista 1: ")
for i in range (c):
    n = int(input(f"Lista 1[{i+1}] =  "))
    lista1.append(n) 
print(f"\nLista 1: {lista1}, con {len(lista1)} términos ")

print(f"\nIngrese los {c} de la lista 2: ")
for i in range (c):
    n = int(input(f"Lista 2[{i+1}] =  "))
    lista2.append(n) 
print(f"\nLista 2: {lista2}, con {len(lista2)} términos ")


print("\nCalculando la suma de las listas ")
for i in range (c):
    lista3.append(lista1[i] + lista2[i])  


print(f"\nLa suma es: {lista3}, con {len(lista3)} términos ")