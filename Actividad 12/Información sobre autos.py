import os; os.system("clear")

autos = [
    {"Marca":"Ford", "Modelo":"Focus", "Año":"2000"},
    {"Marca":"VW", "Modelo":"Jetta", "Año":"2015"}
]

print(autos, len(autos), type(autos))
autos.append({"Marca":"Ford", "Modelo":"Mustang", "Año":1964})
print(autos, len(autos), type(autos))

print("Impresión uno a uno de todos los autos: ")
for auto in autos:
    print(auto)

print("Impresión de datos de un auto en particular: ")
for m,n in autos[0].items():
    print(m,n)

print("Impresión de datos de todos los autos a forma de tabla: ")
for auto in autos:
    for m,n in auto.items():
        print(f"{m:<12} : {n}")
    print()
