import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_tablero_vacio(self):
        # Verifica que al iniciar el juego el tablero esté vacío
        juego = TicTacToe()
        self.assertEqual(juego.tablero, [["", "", ""], ["", "", ""], ["", "", ""]])

    def test_jugada_valida(self):
        # Verifica que una jugada válida se registre correctamente
        juego = TicTacToe()
        self.assertTrue(juego.jugar(0, 0))
        self.assertEqual(juego.tablero[0][0], "X")

    def test_turnos(self):
        # Verifica que los turnos alternan entre X y O correctamente
        juego = TicTacToe()
        juego.jugar(0, 0)  # X
        juego.jugar(1, 1)  # O
        self.assertEqual(juego.tablero[1][1], "O")

    def test_ganador_fila(self):
        # Simula una victoria de X completando la primera fila
        juego = TicTacToe()
        juego.jugar(0, 0)  # X
        juego.jugar(1, 0)  # O
        juego.jugar(0, 1)  # X
        juego.jugar(1, 1)  # O
        juego.jugar(0, 2)  # X gana
        self.assertEqual(juego.ganador, "X")

    def test_empate(self):
        # Simula una partida que termina en empate
        juego = TicTacToe()
        movimientos = [(0,0), (0,1), (0,2), (1,1), (1,0), (1,2), (2,1), (2,0), (2,2)]
        for fila, col in movimientos:
            juego.jugar(fila, col)
        self.assertTrue(juego.es_empate())
        self.assertIsNone(juego.ganador)

    def test_no_sobrescribir_casilla(self):
        # Verifica que no se puede jugar sobre una casilla ocupada
        juego = TicTacToe()
        juego.jugar(0, 0)
        resultado = juego.jugar(0, 0)
        self.assertFalse(resultado)
        self.assertEqual(juego.tablero[0][0], "X")

    def test_ganador_columna(self):
        # Simula una victoria de X completando la primera columna
        juego = TicTacToe()
        juego.jugar(0, 0)  # X
        juego.jugar(0, 1)  # O
        juego.jugar(1, 0)  # X
        juego.jugar(1, 1)  # O
        juego.jugar(2, 0)  # X gana
        self.assertEqual(juego.ganador, "X")

    def test_ganador_diagonal_principal(self):
        # Simula una victoria de X por la diagonal principal (de arriba a abajo)
        juego = TicTacToe()
        juego.jugar(0, 0)  # X
        juego.jugar(0, 1)  # O
        juego.jugar(1, 1)  # X
        juego.jugar(0, 2)  # O
        juego.jugar(2, 2)  # X gana
        self.assertEqual(juego.ganador, "X")

    def test_ganador_diagonal_secundaria(self):
        # Simula una victoria de X por la diagonal secundaria (de arriba derecha a abajo izquierda)
        juego = TicTacToe()
        juego.jugar(0, 2)  # X
        juego.jugar(0, 0)  # O
        juego.jugar(1, 1)  # X
        juego.jugar(1, 0)  # O
        juego.jugar(2, 0)  # X (no completa la diagonal aún)
        juego.jugar(2, 0)  # intento inválido
        juego.jugar(2, 0)  # sigue inválido, se ignora
        # Aunque hay una repetición innecesaria de jugadas inválidas,
        # la siguiente jugada esperada para completar la diagonal sería (2,0),
        # pero ya está ocupada, así que no ganará aquí
        self.assertEqual(juego.ganador, "X")

if __name__ == "__main__":
    unittest.main()
