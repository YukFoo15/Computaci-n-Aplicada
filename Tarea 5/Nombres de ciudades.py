import os; os.system("clear")

print("Lectura de nombres de ciudades")
print("Introduzca los nombres de las ciudades uno por uno.")
print("Escriba '$' cuando haya terminado.")

ciudades = []

while True:
    ciudad = input("Ingrese el nombre de la ciudad: ")
    if ciudad == '$':
        break
    ciudades.append(ciudad)

print("\nCantidad de ciudades:", len(ciudades))
print("Lista completa de ciudades:", ciudades)

ciudades.sort(reverse=True)
print("\nLista de ciudades ordenada en orden descendente:", ciudades)

ciudades_consonantes = [ciudad for ciudad in ciudades if ciudad[0].lower() not in 'aeiou']
print("\nCantidad de ciudades que empiezan con consonante:", len(ciudades_consonantes))
print("Ciudades que empiezan con consonante:", ciudades_consonantes)
