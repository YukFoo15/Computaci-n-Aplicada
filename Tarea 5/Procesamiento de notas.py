import os; os.system("clear")

print("Procesando calificaciones \n")
print("Captura de n calificaciones en un rango de 1 a 10 (escriba 0 para terminar) \n")

nums = []
n = 1
suma = prom = 0

while n != 0:
    n = float(input("Ingrese una calificación: "))
    if n >= 0 and n <= 100:
        nums.append(n)
        suma += n
    else:
        print("Calificación no válida")
        
prom = suma / len(nums) 

max = max(nums)
min = min(nums)


print(f"\nLas {len(nums)} notas capturadas son: {nums} ")
print(f"\nEstadísticas ")
print(f"\nLa suma es: {suma}, el promedio es {prom}")
print(f"\nEl máximo es: {max} mientras que el mínimo es: {min} ")