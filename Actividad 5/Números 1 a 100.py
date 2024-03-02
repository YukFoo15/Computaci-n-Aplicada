import os; os.system("clear")

n = int(input("Introduzca el límite de la sucesión "))
i = int(input("Introduzca el incremento de la sucesión "))

c = 1
while c <= n:
    print(c, end=" ")
    c = c + i
