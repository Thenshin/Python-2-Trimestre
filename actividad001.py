class Jugador:

    #Constructor
    def __init__(self, d, n,):
        self.dorsal = d
        self.nombre = n

    #Metodo de ejemplo
    def mostrar(self):
        print(f"Dorsal: {self.dorsal}, Nombre: {self.nombre}")

Jugador1 = Jugador(10, "Messi")
Jugador1.mostrar()

Jugador2= Jugador(8, "Kobe Bryant")
Jugador2.mostrar()