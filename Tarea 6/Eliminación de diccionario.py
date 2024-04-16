import os
os.system("clear")

municipios = {
    "Apozol": 1863,
    "Calera": 1868,
    "Fresnillo": 1554,
    "Guadalupe": 1821,
    "Jalpa": 1824,
    "Jerez": 1824,
    "Loreto": 1931,
    "Mazapil": 1824,
    "Momax": 1857
}

print("El diccionario de municipios es:", municipios)

del municipios["Apozol"]
print("Después de eliminar Apozol:", municipios)

municipios.pop("Fresnillo")
print("Después de eliminar Fresnillo:", municipios)

municipios.popitem()
print("Después de eliminar Momax:", municipios)

municipios.clear()
print("Después de borrar todos los elementos:", municipios)
