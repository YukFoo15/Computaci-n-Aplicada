import os; os.system("clear")

print("Verificación de promedio \n")
print("Introduzca cinco calificaciones separadas por <Espacio>: ")

c1, c2, c3, c4, c5 = input().split()
c1, c2, c3, c4, c5 = float(c1), float(c2), float(c3), float(c4), float(c5)

suma = c1 + c2 + c3 + c4 + c5
promedio = suma / 5

if promedio >= 0 and promedio < 6:
    print(f"El promedio {promedio} es reprobatorio. ", end="")
elif promedio >= 6 and promedio < 7:
    print(f"El promedio {promedio} es mínimamente aprobatorio. ", end="")
elif promedio >= 7 and promedio < 8:
    print(f"El promedio {promedio} es mejorable. ", end="")
elif promedio >= 8 and promedio < 9:
    print(f"El promedio {promedio} satisfactorio. ", end="")
elif promedio >= 9 or promedio == 10:
    print(f"El promedio {promedio} es excelente. ", end="")



print("\nProceso terminado")