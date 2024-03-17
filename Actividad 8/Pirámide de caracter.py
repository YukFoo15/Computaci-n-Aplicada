import os; os.system("clear")

print("Impresión de una pirámide hecha con el caracter deseado: \n")
car = input("Ingrese el caracter que desea imprimir: ")
n = int(input("Ingrese el número de renglones para la pirámide: "))

for i in range(1, n+1):      
    for j in range(1, i+1):
        print(car, end=" ")
    print("\r")