class Jugador:
    def __init__(self,nombre, fichas=5):
        self.nombre = nombre
        self.fichas = fichas
    
    def __repr__(self) :
        return f"Apuesta: {self.fichas}"

    def darFicha(self, cuantas=1):
        self.fichas = self.fichas + cuantas


                  