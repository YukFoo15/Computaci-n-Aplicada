import os

while True:
    print("Impresión de la conversión de Celsius a Fahrenheit para un rango de valores determinado por el usuario: \n")
    tempI = float(input("Ingrese la temperatura inicial en grados Celsius: "))
    tempF = float(input("Ingrese la temperatura final en grados Celsius: "))

    print("Temperatura (Celsius)   Temperatura (Fahrenheit)")
    celsius = tempI

    while celsius <= tempF:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C                    {fahrenheit}°F")
        celsius += 1

    res = input("¿Desea realizar otra conversión? (S/N): ")
    if res.upper() == "N":
        break
