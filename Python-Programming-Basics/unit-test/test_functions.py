# Test functions
import unittest
import functions_to_test


class FunctionsTestA(unittest.TestCase):

    def setUp(self):
        self.list_1 = [2, 3, 6, 7, 8]
        self.tested_list_1 = [2, 6, 8]
        self.list_2 = [21, 33, 56, 11, 87]
        self.tested_list_2 = [56]
        self.list_3 = [22, 24, 68, 20, 34, 65]
        self.tested_list_3 = [22, 24, 68, 20, 34]

    def test_1(self):
        self.assertEqual(functions_to_test.get_even_numbers(self.list_1), self.tested_list_1, "Fail")

    def test_2(self):
        self.assertEqual(functions_to_test.get_even_numbers(self.list_2), self.tested_list_2, "Fail")

    def test_3(self):
        self.assertEqual(functions_to_test.get_even_numbers(self.list_3), self.tested_list_3, "Fail")


if __name__ == '__main__':
    unittest.main()
