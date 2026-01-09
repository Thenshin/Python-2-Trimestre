class Jugador:

    # Constructor
    def __init__(self, d, n, eq):
        self.dorsal = d
        self.nombre = n
        self.equipo = eq   # mejor nombre para el atributo

    # Método de ejemplo
    def mostrar(self):
        print(f"Dorsal: {self.dorsal}, Nombre: {self.nombre}, Equipo: {self.equipo}")


class Equipo:
    def __init__(self, nom):
        self.nombre_equipo = nom


# --- Programa principal ---
Equipo1 = Equipo("Inter de Miami")
Jugador1 = Jugador(10, "Messi", Equipo1)
Jugador1.mostrar()