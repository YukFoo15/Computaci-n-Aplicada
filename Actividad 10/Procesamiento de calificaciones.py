import os; os.system("clear")

print("Procesando calificaciones \n")
print("Captura de n calificaciones en un rango de 1 a 10 (escriba 99 para terminar) \n")

nums = []
mp = []
n = suma = prom = 0

while n != 99:
    n = float(input("Ingrese una calificación: "))
    if n >= 0 and n <= 10:
        nums.append(n)
        suma += n
    else: 
        print("x")

prom = suma / len(nums)
for i in nums:
    if n >= prom:
        mp.append(n) 


print(f"\nLos {len(nums)} números capturados son: {nums} ")
print(f"\nEstadísticas ")
print(f"\nLa suma es: {suma}, el promedio es {prom} y existen {len(mp)} calificaciones mayores al promedio que son: {mp} ")
print(f"\nEl máximo es: {max(nums)} mientras que el mínimo es: {min(nums)} ")