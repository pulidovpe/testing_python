import unittest
from calculadora import Calculadora

class TestsBasicos(unittest.TestCase):

	def test_calculadora_inicia_en_cero(self):

		calc = Calculadora()
		self.assertEqual(0,calc.valor())

	def test_suma_de_2_mas_3_debe_dar_5(self):

		calc = Calculadora()
		calc.suma(2,3)
		self.assertEqual(5,calc.valor())

	def test_suma_de_4_mas_3_debe_dar_7(self):

		calc = Calculadora()
		calc.suma(4,3)
		self.assertEqual(7,calc.valor())