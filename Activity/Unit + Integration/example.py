import unittest

def a(x):
    return x + 1

def b(x):
    return 2 * x

def c(x):
    return b(a(x))

class SimpleUnitTest(unittest.TestCase):
    def testA(self):
        self.assertEqual(a(3), 4)
    
    def testB(self):
        self.assertEqual(b(3), 6)
    
    def testC(self):
        self.assertEqual(c(3), 8)
        
if __name__ == '__main__':
    unittest.main()