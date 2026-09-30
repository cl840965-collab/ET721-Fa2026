"""
Claudio lopez
Sep 30, 2026
Lab 8: Unit Testing
"""
import unittest 
from calc import *

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2,3), 5)
        self.assertEqual(addtwonumbers(), 0)
        self.assertEqual(addtwonumbers(5), 5)
    def test_sub(self):
        self.assertEqual(subtractingnumbers(5,6),-1)
        self.assertEqual(subtractingnumbers(3),3)
        self.assertEqual(subtractingnumbers(7,3),4)
        self.assertEqual(subtractingnumbers(),0)
    def test_multiplication(self):
        self.assertEqual(multiplynumbers(3,2), 6)
        self.assertEqual(multiplynumbers(5), 5)
        self.assertEqual(multiplynumbers(), 1)

    def test_divison(self):
        self.assertEqual(dividenumbers(7,2), 3.5)
        self.assertAlmostEqual(dividenumbers(7, 3), 2.333, places=3)

    def test_dividebyzero(self):
        self.assertIsNone(dividenumbers(10,0))

    def test_valueerror(self):
        self.assertIsNone(dividenumbers(10, 'a'))
        self.assertIsNone(dividenumbers('a', 10))

    """*def test_unexpected(self):
        with self.assertRaises(Exception):
            dividenumbers()
    """
if __name__ == "__main__":
    unittest.main()