import unittest



class CalcTestCase(unittest.TestCase)
    calculator = Calculator()
    def test_add(self):
        self.assertEqual(4, self.calculator.add(2,2))

if __name__ == "__main__":
    unittest.main()
