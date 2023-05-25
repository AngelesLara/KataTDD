import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto( unittest.TestCase ):
    def test_conjunto_nElementos_retornaPromedioNElementos( self ):
        conjunto=Conjunto([2,4,8,9,10,15])
        self.assertEqual((2+4+8+9+10+15)/6,conjunto.promedio())