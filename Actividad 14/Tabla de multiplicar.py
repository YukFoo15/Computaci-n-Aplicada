def tabla_multiplicar(t, n):
 for i in range(1, n+1):
     print(f'{t} x {i} = {t * i}')

t = int(input('¿Qué tabla desea imprimir?: '))
n = int(input('¿Hasta qué número?: '))
tabla_multiplicar(t, n)