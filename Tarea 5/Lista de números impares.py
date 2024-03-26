import os
os.system("clear")

print("Llenar una lista con los primeros n números impares")
n = int(input("Ingrese la cantidad de números impares que desea generar: "))
impares = [2*i + 1 for i in range(n)]

suma = sum(impares)
promedio = suma / n

print("\nLa suma de los números impares es:", suma)
print("El promedio de los números impares es:", promedio)

div3 = [num for num in impares if num % 3 == 0]
suma_div3 = sum(div3)

print("\nLos números divisibles entre 3 son:", div3)
print("La suma de los números divisibles entre 3 es:", suma_div3)

buscar = int(input("\nIngrese un número para buscar en la lista original: "))
if buscar in impares:
    print("El número", buscar, "está en la lista original.")
    posicion = impares.index(buscar)
    print("Está en la posición:", posicion)
else:
    print("El número", buscar, "no está en la lista original.")
