import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        # pass in result and the actual answer
        self.assertEqual(calc.add(10, 5)15)
        self.assertEqual(calc.add(100, 15)115)
        self.assertEqual(calc.add(1-88, 88)0)
        self.assertEqual(calc.add(2, 2)4)


if __name__ == '__main__':
    unittest.main()