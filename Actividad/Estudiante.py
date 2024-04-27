import os; os.system("clear")

estudiante = {
    "nombre" : "Juan Perez",
    "edad" : 45,
    "email" : "jperez@msn.com",
    "carrera" : "sistemas"
}

print(f"El estudiante \n\n {estudiante}, {len(estudiante)}")

print("\n Las llaves son: ")
for j in estudiante.keys():
    print(j)

print("\n Los valores son: " )
for k in estudiante.values():
    print(k)