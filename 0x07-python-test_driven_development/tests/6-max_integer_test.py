#!/usr/bin/python3

"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Suite test for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def test_empty_list(self):
        """Tests an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        """Testd a list with repeated items"""
        self.assertEqual(max_integer([100, 100, 100]), 100)

    def test_float_numbers(self):
        """Pressernt float in list"""
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def test_max_operated_integer(self):
        """Tset max operation"""
        self.assertEqual(max_integer([-1, -3 * -5, 11, -9]), 25)

    def test_neg_numbers(self):
        """Test negative numbers:"""
        self.assertEqual(max_integer([-5, -9, -2, -1]), -9)

    def test_max_at_beginning(self):
        """Tests list with max number at the beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_zero_number(self):
        """Tests a list with only zeros"""
        self.assertEqual(max_integer([0, 0]), 0)

    def test_list_with_loop(self):
        my_list = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer([i * 2 for i in my_list]), 4)

    def test_one_number_in_a_list(self):
        """Tests a list with only one input/item"""
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        """Tessts a string input"""
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)
