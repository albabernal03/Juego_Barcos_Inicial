import unittest
import juego

class TestJuego(unittest.TestCase):
    def test_jugar_una_partida(self):
        juego.jugar_una_partida()

if __name__ == '__main__':
    unittest.main()