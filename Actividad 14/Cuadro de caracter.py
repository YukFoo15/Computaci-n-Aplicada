def cuadro_caracter(r, c, car):
 for i in range(1, r+1):
     for j in range(1, c+1):
         print(car, end=' ')
     print('\r')

r = int(input('¿ '))
c = int(input('¿Cuántas columnas desea imprimir?: '))
car = input('¿De qué caracter?: ')
cuadro_caracter(r, c, car)