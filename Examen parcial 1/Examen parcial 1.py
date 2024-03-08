import os

print("Universidad Patito S.A. \n")
print("Sistema de Inscripción Congreso de Sistemas \n")
importetot = 0
while True:
    usuario = int(input("Introduzca el tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500: "))
    paquete = int(input("Introduzca el tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900: "))
    cantidad = int(input("Introduzca la cantidad de paquetes deseados: "))

    if usuario == 1:
        cu = 100
        tipoa = "alumnos "
    elif usuario == 2:
        cu = 200
        tipoa = "trabajadores "
    else:
        cu = 500
        tipoa = "docentes "

    if paquete == 1:
        cp = 600
        tipo = "solo para conferencias "
    elif paquete == 2:
        cp = 800
        tipo = "con eventos sociales "
    else:
        cp = 900
        tipo = "con kit de acceso "

    subtotal = (cu + cp) * cantidad

    descuento = 0
    if subtotal > 5000:
        if usuario == 1:
            descuento = 0.2
        elif usuario == 2:
            descuento = 0.1
        elif usuario == 3:
            descuento = 0.05

    total = subtotal
    subtotal -= subtotal * descuento
    importetot += subtotal
    
    print(f"El total de compra: {total} corresponde a: {cantidad} entradas para {tipoa}de costo {cu}, con paquetes {tipo} con costo {cp} y un descuento de {descuento*100}% ({descuento * subtotal}), dando un precio final de {subtotal}")

    res = input("¿Desea continuar? (S/N)")
    if res.upper() == "N": 
        break

print(f"\nLa venta total fue de: {importetot}")

print("\nProceso terminado")
