import os; os.system("clear")

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
paga = [100, 200, 300, 400, 500, 600, 700]

print("Impresión de la paga correspondiente a los diferentes días de la semana \n")

while True: 
    dia = input("Ingrese un día de la semana con letras: ")
    if dia in dias:
        break

print("El día seleccionado para trabajar es: ", dia)
pos = dias.index(dia)
print("La paga correspondiente al día seleccionado es: ", paga[pos])