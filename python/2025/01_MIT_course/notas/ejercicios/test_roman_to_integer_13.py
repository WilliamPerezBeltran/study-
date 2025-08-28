import unittest
from roman_to_integer_13 import Solution

class TestRomanToInteger(unittest.TestCase):
    def test_roman_to_i1(self):
        s = Solution()
        self.assertEqual(s.romanToI("II"), 2)
    
    def test_roman_to_i2(self):
        s = Solution()
        self.assertEqual(s.romanToI("III"), 3)
    
    def test_roman_to_i3(self):
        s = Solution()
        self.assertEqual(s.romanToI("XXVII"), 27)
    
    def test_roman_to_i4(self):
        s = Solution()
        self.assertEqual(s.romanToI("MCMXCIV"), 1994)

if __name__ == "__main__":
    unittest.main()
