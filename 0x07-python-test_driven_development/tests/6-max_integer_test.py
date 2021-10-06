#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class with unittests for max_integerger"""


    def test_types(self):
        """Function that tests types of the args of max_integer"""
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1.2)
        self.assertRaises(TypeError, max_integer, 2 + 5j)
        self.assertRaises(KeyError, max_integer, {'a': 1})
        self.assertRaises(TypeError, max_integer, {1, 2, 3})
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, None)

    def test_values(self):
        """Function that tests the values in the lists of max_integer"""
        self.assertRaises(TypeError, max_integer, [1, 2, 2 + 5j])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, {'a': 1}])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, {1, 2}])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, (1, 2)])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "Jauncho"])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, None])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, [1, 2, 3]])

    def test_max_integer(self):
        """Function that test max_intergers output"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([0, -1, -2]), 0)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-1, -2, 1]), max_integer([-1, -2, True]))
        self.assertEqual(max_integer((-1, -2, 1)), max_integer([-1, -2, 1]))
        self.assertEqual(max_integer("Juancho"), 'u')
        self.assertEqual(max_integer([-1, -2, 1.4]), 1.4)
        self.assertEqual(max_integer([-1, -2, 2, ]), 2)
