class Jugador:
    def __init__(self, nombre, anio_nac, sexo, becado):
        self.nombre = nombre
        self.anio_nac = anio_nac
        self.sexo = sexo
        self.becado = becado
    
    def __str__(self):
        beca_status = "Becado" if self.becado else "Sin Beca"
        sexo = "Hombre" if self.sexo == 'h' else "Mujer"
        return f"Nombre: {self.nombre}, AñoNac: {self.anio_nac}, Sexo: {sexo}, Becado: {beca_status}"

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []
    
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
    
    def total_hombres(self):
        return sum(1 for jugador in self.jugadores if jugador.sexo == 'h')
    
    def total_mujeres(self):
        return sum(1 for jugador in self.jugadores if jugador.sexo == 'm')
    
    def subtotal(self):
        return sum(self.costo for jugador in self.jugadores if not jugador.becado)
    
    def __str__(self):
        return f"Categoría: {self.nombre}, Rango: {self.rango}, Costo: ${self.costo:.2f}, Jugadores: {len(self.jugadores)}"

class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []
    
    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)
    
    def total_categorias(self):
        return len(self.categorias)
    
    def total_hombres(self):
        return sum(categoria.total_hombres() for categoria in self.categorias)
    
    def total_mujeres(self):
        return sum(categoria.total_mujeres() for categoria in self.categorias)
    
    def total_ingresos(self):
        return sum(categoria.subtotal() for categoria in self.categorias)
    
    def __str__(self):
        return (f"Academia: {self.nombre}, Propietario: {self.propietario}, Domicilio: {self.domicilio}\n"
                f"Total de Categorías: {self.total_categorias()}\n"
                f"Total de Hombres: {self.total_hombres()}\n"
                f"Total de Mujeres: {self.total_mujeres()}\n"
                f"Total de Ingresos: ${self.total_ingresos():.2f}")

# Ejemplo de uso
academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")

categoria1 = Categoria("Junior A", "2006/2007/2008", 1250)
categoria1.agregar_jugador(Jugador("Alexander Lopez", 2006, 'h', False))
categoria1.agregar_jugador(Jugador("Uriel Puga", 2007, 'h', True))
categoria1.agregar_jugador(Jugador("Alejandra Escalona", 2008, 'm', False))

categoria2 = Categoria("Junior B", "2009/2010/2011", 850)
categoria2.agregar_jugador(Jugador("Armando Santana", 2009, 'h', False))
categoria2.agregar_jugador(Jugador("Daniel Mijares", 2010, 'h', False))
categoria2.agregar_jugador(Jugador("Antonio Hernandez", 2011, 'm', True))

categoria3 = Categoria("Pony A", "2012/2013/2014", 700)
categoria3.agregar_jugador(Jugador("Andrea Solis", 2012, 'm', True))
categoria3.agregar_jugador(Jugador("Marissa Hernandez", 2013, 'm', True))
categoria3.agregar_jugador(Jugador("Diana Soto", 2014, 'm', False))

academia.agregar_categoria(categoria1)
academia.agregar_categoria(categoria2)
academia.agregar_categoria(categoria3)

print("REPORTE DEL CLUB DEPORTIVO")
print(academia)

print(">> Datos generales de las Categorías")
for categoria in academia.categorias:
    print(f"Nombre: {categoria.nombre} Rango: {categoria.rango} Costo: ${categoria.costo:.2f}")

print(">> Jugadores por Categoría:")
for categoria in academia.categorias:
    print(f"> {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})")
    for jugador in categoria.jugadores:
        print(jugador)
    print(f"- SubTotal : ${categoria.subtotal():.2f}")

print(f"-> Total : ${academia.total_ingresos():.2f}")
