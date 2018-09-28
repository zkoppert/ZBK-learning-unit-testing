import unittest
from Calculator import calculator

class CalcTestDummie(unittest.TestCase):

	def test_alwaysPass(self):
		self.assertTrue(True)

class CalcTestOperations(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calculator.add(2,2),4)

	def test_subtract(self):
		self.assertEqual(calculator.subtract(10,5),5)

if __name__ == "__main__":
    unittest.main()
