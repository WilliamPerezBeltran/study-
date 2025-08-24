import unittest
from tecnical_test01 import(
            no_duplicates,no_duplicates_, no_duplicates__,
            reverse, reverse_, reverse__,
            prime_number,
            highest_grade,
            highest_grade_
        )
class Test01TecnicalTest(unittest.TestCase):

    def test_no_duplicates(self):
        self.assertEqual(no_duplicates([1, 2, 2, 3, 1]),[1, 2, 3])
        self.assertEqual(no_duplicates([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]),[1, 2])

    def test_no_duplicates_(self):
        self.assertEqual(no_duplicates_([1, 2, 2, 3, 1]),[1, 2, 3])
        self.assertEqual(no_duplicates_([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]),[1, 2])

    def test_no_duplicates__(self):
        self.assertEqual(no_duplicates__([1, 2, 2, 3, 1]),[1, 2, 3])
        self.assertEqual(no_duplicates__([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]),[1, 2])

    def test_reverse(self):
        self.assertEqual(reverse("python"),"nohtyp")

    def test_reverse_(self):
        self.assertEqual(reverse_("python"),"nohtyp")

    def test_reverse__(self):
        self.assertEqual(reverse__("python"),"nohtyp")

    def test_prime_number(self):
        self.assertEqual(prime_number(5), True)
        self.assertEqual(prime_number(4), False)
        self.assertEqual(prime_number(661), True)
        self.assertEqual(prime_number(662), False)
        self.assertEqual(prime_number(673), True)

    def test_highest_grade(self):
        self.assertEqual(highest_grade({"Ana": 85, "Luis": 90, "Pedro": 78}), "Luis")
        self.assertEqual(highest_grade_({"Ana": 85, "Luis": 90, "Pedro": 78}), "Luis")
 
if __name__ == "__main__":
    unittest.main()

