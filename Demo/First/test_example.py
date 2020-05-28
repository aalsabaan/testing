import unittest 
  
class SimpleTest(unittest.TestCase): 

    def setUp(self): 
        pass
    
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')
    
    def test_fail_message(self):
        self.assertTrue(False, 'failure message goes here')
  
if __name__ == '__main__': 
    unittest.main() 
