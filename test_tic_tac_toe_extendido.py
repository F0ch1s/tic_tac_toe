import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToeExtendido(unittest.TestCase):

    def test_tablero_configurable(self):
        # Verifica que el tamaño del tablero se configure correctamente al iniciar
        juego = TicTacToe(5)
        self.assertEqual(len(juego.tablero), 5)
        self.assertEqual(len(juego.tablero[0]), 5)

    def test_longitud_ganadora_pequeno(self):
        # Para tableros < 5x5, la victoria se logra con 3 en raya
        juego = TicTacToe(4)
        self.assertEqual(juego.longitud_ganadora, 3)

    def test_longitud_ganadora_grande(self):
        # Para tableros >= 5x5, la victoria se logra con 4 en raya
        juego = TicTacToe(6)
        self.assertEqual(juego.longitud_ganadora, 4)

    def test_ganador_horizontal_3_en_raya(self):
        # Simula una victoria horizontal de X en tablero 4x4
        juego = TicTacToe(4)
        juego.jugar(1, 0)  # X
        juego.jugar(0, 0)  # O
        juego.jugar(1, 1)  # X
        juego.jugar(0, 1)  # O
        juego.jugar(1, 2)  # X gana
        self.assertEqual(juego.ganador, "X")

    def test_ganador_vertical_4_en_raya(self):
        # Simula victoria vertical de X en tablero 5x5
        juego = TicTacToe(5)
        juego.jugar(0, 0)
        juego.jugar(0, 1)
        juego.jugar(1, 0)
        juego.jugar(1, 1)
        juego.jugar(2, 0)
        juego.jugar(2, 1)
        juego.jugar(3, 0)  # X gana con 4 en columna
        self.assertEqual(juego.ganador, "X")

    def test_ganador_diagonal_4_en_raya(self):
        # Simula victoria diagonal de X en tablero 5x5 (de izquierda a derecha)
        juego = TicTacToe(5)
        juego.jugar(0, 0)
        juego.jugar(0, 1)
        juego.jugar(1, 1)
        juego.jugar(0, 2)
        juego.jugar(2, 2)
        juego.jugar(0, 3)
        juego.jugar(3, 3)  # X gana con 4 en diagonal
        self.assertEqual(juego.ganador, "X")

    def test_empate_tablero_3x3(self):
        # Simula una partida completa en 3x3 sin ganador (empate)
        juego = TicTacToe(3)
        movimientos = [(0,0), (0,1), (0,2), (1,1), (1,0), (1,2), (2,1), (2,0), (2,2)]
        for fila, col in movimientos:
            juego.jugar(fila, col)
        self.assertTrue(juego.es_empate())
        self.assertIsNone(juego.ganador)

    def test_reinicio_mantiene_tamano(self):
        # Verifica que el reinicio del juego no cambia el tamaño del tablero
        juego = TicTacToe(6)
        juego.jugar(0, 0)
        juego.reiniciar()
        self.assertEqual(len(juego.tablero), 6)
        self.assertEqual(juego.ganador, None)
        self.assertEqual(juego.turno, "X")

    def test_ia_gana_si_puede(self):
        # Verifica que la IA (jugador O) aprovecha una oportunidad de victoria
        juego = TicTacToe(3)
        juego.tablero = [
            ["O", "O", ""],
            ["X", "X", ""],
            ["", "", ""]
        ]
        juego.turno = "O"
        fila, col = juego.obtener_jugada_maquina()
        self.assertEqual((fila, col), (0, 2))  # La IA debe colocar la O en (0,2) para ganar

    def test_ia_bloquea_amenaza(self):
        # Verifica que la IA bloquea al jugador X si está por ganar
        juego = TicTacToe(3)
        juego.tablero = [
            ["X", "X", ""],
            ["O", "", ""],
            ["", "", ""]
        ]
        juego.turno = "O"
        fila, col = juego.obtener_jugada_maquina()
        self.assertEqual((fila, col), (0, 2))  # La IA debe bloquear en (0,2)

    def test_ia_juega_casilla_libre(self):
        # Verifica que la IA elige una celda vacía si no hay amenazas ni oportunidad directa
        juego = TicTacToe(3)
        juego.tablero = [
            ["X", "O", "X"],
            ["", "", ""],
            ["", "", ""]
        ]
        juego.turno = "O"
        fila, col = juego.obtener_jugada_maquina()
        self.assertEqual(juego.tablero[fila][col], "")  # El movimiento debe ser en una celda libre


if __name__ == "__main__":
    unittest.main()
