import os; os.system("clear")

lim = int(input("Introduzca el límite de la sucesión: "))
incremento = int(input("Introduzca el incremento de la sucesión: "))
print(f"imprimiendo números del 1 al {lim} de {incremento} en {incremento}: ")


for i in range (1, lim+1, incremento):
    print(i, end=" ")
