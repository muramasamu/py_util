import unittest

class TestStartsWithA(unittest.TestCase):
    def test_starts_with_A(self):
        self.assertTrue(starts_with_C('Amazon'))
        self.assertFalse(starts_with_C('Dog'))
        self.assertFalse(starts_with_C(''))
        self.assertFalse(starts_with_C(None))

if __name__ == '__main__':
    unittest.main()
