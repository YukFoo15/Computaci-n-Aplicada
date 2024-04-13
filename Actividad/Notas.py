import os; os.system("clear")

materias = ["Física", "Química", "Matemáticas", "Geografía", "Estadística"]
calis = [10,9,8,7.5,6]

print(f"Materias:  {materias}, {len(materias)}")
print(f"Calificaciones:  {calis}, {len(calis)}")


notas = dict(zip(materias, calis))
print(f"Las notas son:  {notas}, {len(notas)}")

notas.update({"Inglés":10})
notas["Programación"] = 7
print(f"Las notas {notas}, {len(notas)}")

notas.pop("Física")
notas.popitem()
print(f"Las notas son: {notas}, {len(notas)}")

notas["Química"] = 10
notas.update({"Matemáticas":10, "Geografía":10})
print(f"Las notas son: {notas}, {len(notas)}")

print(f"\n Lista de materias, suma y promedio: " )
s = p = 0

for m, c in notas.items():
    print(f"{m:<12} - {c:5}")
    s = s + c
p = s / len(notas)

print(f"La suma es: {s} y el promedio es: {p}")

notas.clear()
print(f"Las notas son: {notas}, {len(notas)} ")