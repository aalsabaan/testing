import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.std1 = Student(first="Halah", last="AlMazrua", language="Python")

    def test_fullname(self):
        self.assertEqual(self.std1.fullname, 'Halah-AlMazrua')

    def test_email(self):
        self.assertEqual(self.std1.email, 'Halah.AlMazrua@company.com')

if __name__ == "__main__":
    unittest.main()