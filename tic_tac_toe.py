import random
import copy

class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.tablero = [["" for _ in range(size)] for _ in range(size)]
        self.turno = "X"
        self.ganador = None
        self.longitud_ganadora = 3 if size < 5 else 4

    def jugar(self, fila, columna):
        if self.tablero[fila][columna] == "" and self.ganador is None:
            self.tablero[fila][columna] = self.turno
            if self.verificar_ganador(fila, columna):
                self.ganador = self.turno
            else:
                self.turno = "O" if self.turno == "X" else "X"
            return True
        return False

    def verificar_ganador(self, fila, columna):
        simbolo = self.tablero[fila][columna]
        n = self.size
        r = self.longitud_ganadora

        def contar_en_direccion(df, dc):
            count = 1
            for dir in [1, -1]:
                i = 1
                while True:
                    f = fila + dir * df * i
                    c = columna + dir * dc * i
                    if 0 <= f < n and 0 <= c < n and self.tablero[f][c] == simbolo:
                        count += 1
                        i += 1
                    else:
                        break
            return count

        # Revisa horizontal, vertical y las dos diagonales
        direcciones = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for df, dc in direcciones:
            if contar_en_direccion(df, dc) >= r:
                return True
        return False

    def es_empate(self):
        return all(cell != "" for row in self.tablero for cell in row) and self.ganador is None

    def reiniciar(self):
        self.__init__(self.size)

    def obtener_jugada_maquina(self):
        for fila in range(self.size):
            for col in range(self.size):
                if self.tablero[fila][col] == "":
                    copia = copy.deepcopy(self.tablero)
                    copia[fila][col] = self.turno
                    if self._es_ganador_simulado(copia, fila, col, self.turno):
                        return fila, col

        oponente = "O" if self.turno == "X" else "X"
        for fila in range(self.size):
            for col in range(self.size):
                if self.tablero[fila][col] == "":
                    copia = copy.deepcopy(self.tablero)
                    copia[fila][col] = oponente
                    if self._es_ganador_simulado(copia, fila, col, oponente):
                        return fila, col

        vacias = [(f, c) for f in range(self.size) for c in range(self.size) if self.tablero[f][c] == ""]
        return random.choice(vacias) if vacias else (None, None)

    def _es_ganador_simulado(self, tablero_simulado, fila, columna, simbolo):
        def contar_en_direccion(df, dc):
            count = 1
            for dir in [1, -1]:
                i = 1
                while True:
                    f = fila + dir * df * i
                    c = columna + dir * dc * i
                    if 0 <= f < self.size and 0 <= c < self.size and tablero_simulado[f][c] == simbolo:
                        count += 1
                        i += 1
                    else:
                        break
            return count

        for df, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            if contar_en_direccion(df, dc) >= self.longitud_ganadora:
                return True
        return False
