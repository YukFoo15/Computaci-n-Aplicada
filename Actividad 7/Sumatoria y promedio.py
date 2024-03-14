import os; os.system("clear")

print("Sumatoria y promedio de n calificaciones introducidos por el usuario:\n")
n = int(input("Introduzca el número de calificaciones a sumar/promediar: "))

suma = promedio = 0
for i in range (1, n+1):
    print(f"calificación {i}.",  end=" ")
    c = float(input())
    suma = suma + c

promedio = suma / n
print(f"La suma de las calificaciones es: {suma}. Mientras que el promedio es: {promedio}")