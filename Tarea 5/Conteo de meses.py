import os; os.system("clear")

meses = ["enero","febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print("Impresión del número de días de cada mes")
m = int(input("Introduzca número correspondiente al mes deseado: "))


if m >= 1 and m <= 12:
    print(f"El número de días en el mes {meses[m]} es: {dias[m]}")

else:
    print("Número inválido")
