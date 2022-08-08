from asyncio import exceptions
import unittest

from django.test import TestCase
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        print('test1')
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        # to run this we need to run this command.
        # python -m unittest test_calc.py
    def test_add1(self):
        print('test2')
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(100, 5), 105)
        self.assertEqual(calc.add(1000, 5), 1005)
        self.assertEqual(calc.add(10, -5), 5)
        self.assertEqual(calc.add(-10, -10), -20)

    def test_sub(self):
        print('test3')
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(100, 5), 95)
        self.assertEqual(calc.sub(1000, 5), 995)
        self.assertEqual(calc.sub(10, -5), 15)
        self.assertEqual(calc.sub(-10, -10), 0)

    def test_mul(self):
        print('test4')
        self.assertEqual(calc.mul(10, 5), 50)
        self.assertEqual(calc.mul(100, 5), 500)
        self.assertEqual(calc.mul(1000, 5), 5000)
        self.assertEqual(calc.mul(10, -5), -50)
        self.assertEqual(calc.mul(-10, -10), 100)

    def test_div(self):
        print('test5')
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(100, 5), 20)
        self.assertEqual(calc.div(1000, 5), 200)
        self.assertEqual(calc.div(10, -5), -2)
        self.assertEqual(calc.div(-10, -10), 1)

        self.assertRaises(ValueError, calc.div, 10, 0) 
        # this is for checking exceptions

        with self.assertRaises(ValueError):
            calc.div( 10, 2)
        # Same as the previous code but using context manager, it is the most preferred method for doing tests.
        


if __name__ == '__main__':
    unittest.main()

    # to run as ::    python test_calc.py