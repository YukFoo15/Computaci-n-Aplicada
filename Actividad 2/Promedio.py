sum = 0
c = int(input("Introduzca el número de calificaciones a las que se les obtendrá el promedio: ") )

for i in range(0,c):
  cal = int(input("Introduzca una calificación: ") )
  sum = sum + cal

promedio = sum / c

print("El promedio de las calificaciones ingresadas es: ", promedio)