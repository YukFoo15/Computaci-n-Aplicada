import os; os.system("clear")

print("Verificación de un número para positivos negativos y cero \n")

n = int(input("Introduzca el número a verificar: "))


if n > 0:
    print("El número es positivo")

if n < 0:
    print("El número es negativo")

if n == 0:
    print("El número es cero")

print("Proceso terminado")