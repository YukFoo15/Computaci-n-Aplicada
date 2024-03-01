import os; os.system("clear")

print("Cálculo de los valores de la segunda ley de Newton \n")
print("[ f ] = m * a")
print("[ m ] = f / a")
print("[ a ] = f / m")
op = input("Elige una opción ?").lower()

if op == "f":
    print("\nCalculando la fuerza...")
    m = float(input("Introduzca el valor de la masa "))
    a = float(input("Introduzca el valor de la aceleración "))
    f = m * a 
    print("La fuerza es: ", f)

elif op == "m":
    print("\nCalculando la masa...")
    f = float(input("Introduzca el valor de la fuerza "))
    a = float(input("Introduzca el valor de la aceleración "))
    m = f / a 
    print("La masa es: ", m)

elif op == "a":
    print("\nCalculando la aceleración...")
    f = float(input("Introduzca el valor de la fuerza "))
    m = float(input("Introduzca el valor de la masa "))
    a = f / m 
    print("La aceleración es: ", a)

else: 
    print("\nOpción incorrecta")

print("\nProceso terminado")