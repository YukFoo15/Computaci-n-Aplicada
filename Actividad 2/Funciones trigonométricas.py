import os
import math


os.system("clear")

print("Cálculo de funciones trigonométricas \n")
angulo = float(input("Introduzca el valor del ángulo a considerar (en radianes): "))

seno = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

grados = math.degrees(angulo)

salida = (
    "\nResumen de funciones trigonométricas \n"
    f"El seno: {seno}\n"
    f"El coseno: {cos}\n"
    f"La tangente: {tan}\n"
    f"\nEl ángulo {angulo} en radianes, equivale a {grados}°"
)


print(salida)
