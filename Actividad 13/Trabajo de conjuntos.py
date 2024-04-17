import os
os.system("clear")

municipios = {"Zacatecas","Guadalupe", "Jerez","Fresnillo"}

print("Conjuntos y operaciones sobre municipios")
print(f"{municipios} {len(municipios)} {type(municipios)}")
print("\nAcceso al conjunto de municipios utilizando un ciclo: ")

for m in municipios:
    print(m.upper())
print("Agregación de elementos al conjunto: ")
municipios.add("Teúl")
municipios.update({"Luis Moya", "Tepetongo"})
print(f"{municipios} {len(municipios)} {type(municipios)}")
print("Eliminación de elementos del conjunto: ")
municipios.remove("Zacatecas")
municipios.discard("Ojocaliente")
municipios.pop()
print(f"{municipios} {len(municipios)} {type(municipios)}")
print("Eliminación de todos los elementos del conjunto: ")
municipios.clear()
print(f"{municipios} {len(municipios)} {type(municipios)}")