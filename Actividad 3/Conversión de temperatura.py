import os; os.system("clear")

print("Conversor de temperatura Farenheit a Celsius \n")
opcion = str.upper(input("[C] elsius \n[F] arenheit \nElija?"))

if opcion == "C":
    print("\nConvirtiendo a Celsius...")
    temp = float(input("Grados Farenheit? "))
    res = (temp - 32)*5 / 9
    print(f"{temp} grados Farenheit, equivale a {res} grados Celsius")

else:
    print("\nConvirtiendo a Farenheit...")
    temp = float(input("Grados Celsius? "))
    res = (temp * 9/5) + 32
    print(f"{temp} grados Celsius, equivale a {res} grados Farenheit")

print("\nProceso terminado")