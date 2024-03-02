import os; os.system("clear")

n = int(input("Introduzca el inicio de la sucesión "))
i = int(input("Introduzca el incremento de la sucesión "))

c = n
while c >= 1:
    print(c, end=" ")
    c = c - i
