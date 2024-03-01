import os; os.system("clear")

print("Clasificador de ángulos segúun su magnitud \n")
angulo = int(input("Introduzca su el ángulo "))

if angulo >= 0  and angulo <= 360:
    print(f"El ángulo tiene {angulo} grados, por lo tanto es un ángulo: ", end="")
    if angulo < 90:
        print("Agudo")
    elif angulo == 90:
        print("Recto")
    elif angulo > 90 and angulo < 180:
        print("Obtuso")
    elif angulo == 180:
        print("Llano")
    elif angulo > 180 and angulo < 360:
        print("Concavo")
    else:
        print("Completo")
        
else:
    print("\nFuera de rango")

print("\nProceso terminado")