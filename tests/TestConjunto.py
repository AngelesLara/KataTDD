import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto( unittest.TestCase ):
    def test_conjunto_dosElementos_retornaPromedioElementos(self):
        conjunto = Conjunto([5, 7])
        self.assertEqual(6, conjunto.promedio())
