from unittest import TestCase

from mind_geometry.areas import area


class MainAreaCalcInterfaceTest(TestCase):
    def test_area_calculated_correctly(self):
        expected = {
            (3, 4, 5): 6,
            (39, 41.1, 8): 153.8,
            (1, 1, 1): 0.43,
            (1,): 3.14,
            (2,): 12.56,
            (5.14,): 82.99
        }

        for args, result in expected.items():
            with self.subTest(args=args, result=result):
                self.assertAlmostEqual(area(*args), result, 1)

    def test_area_get_incorrect_number_of_args(self):
        invalid_args = [(2, 2), (11, 4, 5, 6), (90, 1, 1, 1, 1), tuple()]

        for args in invalid_args:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    area(*args)        