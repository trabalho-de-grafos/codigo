import unittest

def soma(a,b):
    return a+b

class UnitTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_soma(self):
        self.assertEqual(2, soma(1,1))




if __name__ == '__main__':
    unittest.main()
