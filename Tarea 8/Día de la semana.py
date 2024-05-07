def obtener_dia_semana(numero):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }

    return dias.get(numero, "Número inválido")

def main():
    numero = int(input("Ingrese un número entero entre 1 y 7: "))
    dia_semana = obtener_dia_semana(numero)
    print(f"El día correspondiente al número {numero} es: {dia_semana}")

if __name__ == "__main__":
    main()