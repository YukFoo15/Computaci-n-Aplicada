def suma(n1, n2):
 return n1 + n2
print('\nSuma de dos números constantes: ')
print(suma(100,200))
print('Ingrese dos números para sumarlos: ')
a,b = int(input()), int(input())
print(f"La suma de los números es {suma(a,b)}")