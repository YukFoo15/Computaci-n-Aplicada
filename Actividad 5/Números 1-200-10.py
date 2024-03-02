import os; os.system("clear")

m = int(input("Introduzca los múltiplos de la sucesión "))

c = 0
while c <= 200:
    c += 1
    if c % m != 0:
        continue
    print(c, end=" ")