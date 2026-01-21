class Equipo:
    def __init__(self, nombre):
        self.nombre_equipo = nombre
        self.jugadores_eq = []

    def agregar_jugador(self, jugador):
        self.jugadores_eq.append(jugador)

    def mostrar_jugadores(self):
        print(f"\nEquipo: {self.nombre_equipo}")
        for jugador in self.jugadores_eq:
            jugador.mostrar()


class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = None

    def asignar_equipo(self, equipo):
        self.equipo = equipo
        equipo.agregar_jugador(self)

    def mostrar(self):
        print(f"Dorsal: {self.dorsal}, Nombre: {self.nombre}, Equipo: {self.equipo.nombre_equipo}")

    def guardar_en_txt(self):
        with open("jugadores.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"Dorsal: {self.dorsal}, "
                f"Nombre: {self.nombre}, "
                f"Equipo: {self.equipo.nombre_equipo}\n"
            )


# ===== PROGRAMA PRINCIPAL =====

# Pedir datos al usuario
nombre_jugador = input("Introduce el nombre del jugador: ")
dorsal_jugador = input("Introduce el dorsal del jugador: ")
nombre_equipo = input("Introduce el nombre del equipo: ")

# Crear objetos
equipo = Equipo(nombre_equipo)
jugador = Jugador(dorsal_jugador, nombre_jugador)

# Asignar equipo
jugador.asignar_equipo(equipo)

# Mostrar por pantalla
print("\n--- Datos del jugador ---")
jugador.mostrar()

# Guardar en archivo .txt
jugador.guardar_en_txt()

print("\nDatos guardados correctamente en jugadores.txt")

