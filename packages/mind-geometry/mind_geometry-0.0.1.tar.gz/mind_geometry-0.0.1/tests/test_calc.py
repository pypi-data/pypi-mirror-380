from unittest import TestCase

from mind_geometry.figures import Circle, Triangle


class CircleTest(TestCase):      
    def test_get_area_valid(self):
        expected = {
            '1': 3.14,
            '2': 12.56,
            '5.14': 82.99
            }

        for arg, result in expected.items():
            with self.subTest(arg=arg, result=result):
                circle = Circle(float(arg))
                self.assertAlmostEqual(circle.get_area(), result, 1)


class TriangleTest(TestCase):      
    def test_get_area_valid(self):
        expected = {
            (3, 4, 5): 6,
            (39, 41.1, 8): 153.8,
            (1, 1, 1): 0.43
            }

        for args, result in expected.items():
            with self.subTest(args=args, result=result):
                triangle = Triangle(*args)
                self.assertAlmostEqual(triangle.get_area(), result, 1)

    def test_is_right(self):
        expected = {
            (4, 4, 2): False,
            (3, 4, 5): True,
            (1, 1, 1): False,
            
        }

        for args, result in expected.items():
            with self.subTest(args=args, result=result):
                triangle = Triangle(*args)
                self.assertAlmostEqual(triangle.is_right(), result, 1)

