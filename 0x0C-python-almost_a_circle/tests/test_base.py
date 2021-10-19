#!/usr/bin/python3
import unittest


class TestBase(unittest.TestCase):
    """Tests for Base class"""
    def test_01_case_instance_fail_01(self):
        new_obj1 = {"size": 5}
        self.assertIsNot(new_obj1, (Rectangle, Square))
    def test_01_case_instance_fail_02(self):
        new_obj1 = {"width": 5, "height": 13}
        self.assertIsNot(new_obj1, (Rectangle, Square))
    def test_02_type_from_json_string_success(self):
        new_obj = Rectangle(2, 3)
        to_string = '[{"id": 1, "width": 10, "_Rectangle__height": 7, "_Rectangle__x": 2, "_Rectangle__y": 8}, {"id": 2, "_Rectangle__width": 2, "_Rectangle__height": 4, "_Rectangle__x": 0, "_Rectangle__y": 0}]'
        result = new_obj.from_json_string(to_string)
        self.assertEqual(type(result), list)
    def test_03_create_rquare_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsInstance(new_obj2, Square)
    def test_03_create_rectangle_success(self):
        new_obj1 = Rectangle(5, 2)
        dictionary = {"width": 10, "height": 5, "x": 2, "y": 2}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsInstance(new_obj2, Rectangle)
    def test_03_create_rquare_fail(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsNot(new_obj2, Rectangle)
    def test_03_create_rectangle_fail(self):
        new_obj1 = Rectangle(5, 2)
        dictionary = {"width": 10, "height": 5, "x": 2, "y": 2}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsNot(new_obj2, Square)
    def test_04_create_size_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertEqual(new_obj2.size, 10)
    def test_04_create_x_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        new_obj2.x = 15
        self.assertEqual(new_obj2.x, 15)
    def test_set_id_none(self):
        b_cero = Base()
        self.assertEqual(b_cero.id, 2)
    def test_set_id_none_fail(self):
        b_one = Base()
        self.assertNotEqual(b_one.id, 74)
    def test_set_id_74(self):
        b = Base(74)
        self.assertEqual(b.id, 74)
    def test_set_id_74_fail(self):
        b74 = Base()
        self.assertNotEqual(b74.id, 74)
    def test_private(self):
        b_private = Base(3)
        with self.assertRaises(AttributeError):
            print(b_private.nb_objects)
        with self.assertRaises(AttributeError):
            print(b_private.__nb_objects)
    def test_to_json_string(self):
        Base._Base__nb_objects = 0
        b1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        b2 = {"id": 5, "width": 4, "height": 3, "x": 2, "y": 1}
        json_s = Base.to_json_string([b1, b2])
        self.assertTrue(type(json_s) is str)
        b0 = json.loads(json_s)
        self.assertEqual(b0, [b1, b2])
    def test_from_json_string_empty(self):
        self.assertEqual([], Base.from_json_string(""))
    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))
    def test_from_json_string(self):
        """Tests normal from_json_string"""
        json_str = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, \
                     {"id": 5, "width": 4, "height": 3, "x": 2, "y": 1}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertEqual(json_l[0], {"id": 1, "width": 2, "height": 3,
                                     "x": 4, "y": 5})
        self.assertEqual(json_l[1], {"id": 5, "width": 4, "height": 3,
                                     "x": 2, "y": 1})
