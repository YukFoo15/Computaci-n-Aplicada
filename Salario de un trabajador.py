# Programa que calcula el salario de un trabajador respecto a las horas y salario determinados por el usuario.

nombre = str(input("Introduzca el nombre del trabajador:"))
salh = float(input("Introduzca el salario por hora del trabajador:"))
hor = int(input("Introduzca las horas trabajadas:"))
salariof = (salh*hor)
print("El salario final es:", salariof)