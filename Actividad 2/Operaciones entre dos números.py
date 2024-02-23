import os; os.system("clear")

print("Operaciones entre dos números flotantes \n")

x = float(input("Introduzca el valor de x: ") )
y = float(input("Introduzca el valor de y: ") )

suma = x + y
resta = x - y
mult = x * y
div = x / y
res = x % y
exp = x ** y
dive = x // y

print(f"Suma:{suma}\nResta:{resta}\nMultiplicación:{mult}\nDivisión:{div}\nResiduo:{res}\nExponenciación:{exp}\nDivisión entera:{dive}\n")