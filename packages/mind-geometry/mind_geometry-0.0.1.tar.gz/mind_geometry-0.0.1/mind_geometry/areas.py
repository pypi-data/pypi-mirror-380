from .factory import FigureFactory
from .figures import Figure


def area(*args, **kwargs):
    factory = FigureFactory()
    figure: Figure = factory(*args, **kwargs)
    return figure.get_area()