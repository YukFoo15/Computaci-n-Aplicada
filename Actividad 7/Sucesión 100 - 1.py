import os; os.system("clear")

lim = int(input("Introduzca el límite de la sucesión: "))
decremento = int(input("Introduzca el decremento de la sucesión: "))
print(f"imprimiendo números del {lim} al 1 de {decremento} en {decremento}: ")


for i in range (lim, 0, -decremento):
    print(i, end=" ")
