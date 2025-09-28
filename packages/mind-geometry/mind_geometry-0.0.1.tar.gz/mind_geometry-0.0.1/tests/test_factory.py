from unittest import TestCase

from mind_geometry.factory import FigureFactory
from mind_geometry.figures import Triangle, Circle


class FigureFactoryTest(TestCase):
    def setUp(self) -> None:
        self.factory = FigureFactory()

    def test_figure_definition(self):
        expected = {
            (3, 5, 8): Triangle,
            (1, ): Circle,
            (1, 1, 1): Triangle,
            (5,): Circle,
        }

        for args, result in expected.items():
            with self.subTest(args=args, result=result):
                self.assertIsInstance(self.factory(*args), result)