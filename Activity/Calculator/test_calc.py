import unittest
import calc

class TestCalc(unittest.TestCase):

    def setUp(self): 
        pass

    def test_add(self):
        response = calc.add(10, 5)
        self.assertEqual(response, 15)
        response = calc.add(-1, 1)
        self.assertEqual(response, 0)
        response = calc.add(-1, -1)
        self.assertEqual(response, -2)

    def test_subtract(self):
        response = calc.subtract(10, 5)
        self.assertEqual(response, 5)
        response = calc.subtract(-1, 1)
        self.assertEqual(response, -2)
        response = calc.subtract(-1, -1)
        self.assertEqual(response, 0)

    def test_multiply(self):
        response = calc.multiply(10, 5)
        self.assertEqual(response, 50)
        response = calc.multiply(-1, 1)
        self.assertEqual(response, -1)
        response = calc.multiply(-1, -1)
        self.assertEqual(response, 1)
    
    def test_volume(self):
        self.assertAlmostEqual(calc.cuboid_volume(2),8)
        self.assertAlmostEqual(calc.cuboid_volume(1),1)
        self.assertAlmostEqual(calc.cuboid_volume(0),0)
        self.assertAlmostEqual(calc.cuboid_volume(5.5),166.375)

if __name__ == '__main__':
    unittest.main()