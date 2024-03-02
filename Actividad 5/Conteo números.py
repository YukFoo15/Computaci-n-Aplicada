import os; os.system("clear")

cuenta = suma = 0
cp = cn = cz = 0

print("Conteo de números:\n")


while (True):
    num = int(input("Introduzca el número "))
    if num != 999:
        cuenta = cuenta + 1
        suma = suma + num
        if num > 0: cp += 1
        elif num < 0 : cn += 1
        else : cz +=1
    else:   
        break

print(f"Se introdujeron {cuenta} números")
print(f"La suma es {suma}")
print(f"Positivos: {cp}, Negativos: {cn}, Ceros: {cz}")