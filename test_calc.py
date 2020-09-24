import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        # pass in result and the actual answer
        self.assertEqual(calc.add(10, 5),15)
        self.assertEqual(calc.add(100, 15),115)
        self.assertEqual(calc.add(-88, 88),0)
        self.assertEqual(calc.add(2, 2),4)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(2, 5), -3)
        self.assertEqual(calc.subtract(10, 2), 8)
        self.assertEqual(calc.subtract(7, 5), 2)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(2, 5), 10)
        self.assertEqual(calc.multiply(10, 2), 20)
        self.assertEqual(calc.multiply(7, 5), 35)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(8, 2), 4)
        self.assertEqual(calc.divide(9, 3), 3)
        self.assertEqual(calc.divide(50, 10), 5)
        # self.assertRaises(ValueError, calc.divide, 10, 0)

        with self.assertRaises(ValueError):
            n = 10
            l = 0
            calc.divide(n, l)

     
if __name__ == '__main__':
    unittest.main()