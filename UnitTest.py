# Unit testing is a type of testing that focuses on individual units or components of a software application. The following example demonstrates how to use the unittest module in Python to write and run unit tests
import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
