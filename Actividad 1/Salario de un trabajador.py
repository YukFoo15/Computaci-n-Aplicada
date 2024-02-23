# Programa que calcula el salario de un trabajador respecto a las horas y salario determinados por el usuario.

nombre = str(input("Introduzca el nombre del trabajador:"))
salh = float(input("Introduzca el salario por hora del trabajador:"))
hor = int(input("Introduzca las horas trabajadas:"))
salario = (salh*hor)
tasa = 0.3
impuesto = tasa * salario
salariof = salario - impuesto




print("El/La trabajador/a {nombre} trabajó {horas} con un salario por hora de {salh} y una tasa de impuestos del {tasa}% dando un salario final de: ", salariof) 