import unittest
from calculadora import Calculadora

class TestsBasicos(unittest.TestCase):

	def test_calculadora_inicia_en_cero(self):

		calc = Calculadora()
		self.assertEqual(0,calc.valor())