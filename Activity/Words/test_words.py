import unittest
import words

class TestWords(unittest.TestCase):

    def setUp(self): 
        pass

    # Returns True if the string contains 4 a. 
    def test_lower(self): 
        self.assertEqual('halah', words.lowercase('HALAH')) 
  
    # Returns True if the string is in upper case. 
    def test_upper(self):
        self.assertEqual('HALAH', words.uppercase('halah')) 
    
if __name__ == '__main__': 
    unittest.main() 