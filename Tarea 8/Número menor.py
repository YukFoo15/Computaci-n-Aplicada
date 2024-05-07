def menor_de_tres(num1, num2, num3):
    menor = num1
    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3
    return menor

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

resultado = menor_de_tres(numero1, numero2, numero3)
print(f"El menor de los tres números es: {resultado}")
