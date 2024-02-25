import os; os.system("clear")


print("Conversor de horas a días, minutos y segundos\n")

horas = float(input("Ingrese la cantidad de horas: "))

dias = horas / 24
minutos = horas * 60
segundos = horas * 3600

print(f"\n{horas} horas equivalen a:")
print(f"Días: {dias}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")
