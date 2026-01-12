class Equipo:
    def __init__(self, nombre):
        self.nombre_equipo = nombre
        self.jugadores_eq= []

    def agregar_jugador(self,jugador) :
        self.jugadores_eq.append(jugador)

class Jugador:
    def __init__(self, dor, nom) :
        self.dorsal = dor
        self.nombre = nom
        self.equipo = None

    def asignar_equipo(self, equipo) :
        self.equipo = equipo
        equipo.agregar_jugador(self)

    def mostrar(self):
        print(f"Dorsal: {self.dorsal}, Nombre: {self.nombre}")

equipo1=Equipo("Inter de Miami")
equipo2=Equipo("Los Angeles Lakers")
equipo3=Equipo("FC Barcelona")

Jugador1 = Jugador(10, "Messi")
Jugador1.asignar_equipo(equipo1)
Jugador1.mostrar()

Jugador2= Jugador(8, "Kobe Bryant")
Jugador2.asignar_equipo(equipo2)
Jugador2.mostrar()

Jugador3= Jugador(8, "Hristo Stoychkov")
Jugador3.asignar_equipo(equipo3)
Jugador3.mostrar()


print(f"Equipo:{equipo2.nombre_equipo}")
for jugador in equipo2.jugadores_eq :
    jugador.mostrar()