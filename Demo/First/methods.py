import unittest 
  
class SimpleTest(unittest.TestCase): 

    def setUp(self): 
        print('setUp Method')
    
    @classmethod
    def setUpClass(self): 
        print('setUpClass Method')
    
    def tearDown(self): 
        print('tearDown Method')
    
    @classmethod
    def tearDownClass(self): 
        print('tearDownClass Method')
    
    def test_pass_one(self):
        self.assertTrue(True)
    
    def test_pass_two(self):
        self.assertTrue(True)
    
    @unittest.skip("reason for skipping")
    def test_skip(self):
        self.assertTrue(False)
  
if __name__ == '__main__': 
    unittest.main() 


    