from typing import Any

from .figures import Circle, Triangle


class FigureFactory:
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if len(args) + len(kwargs) == 1:
            return Circle(*args, **kwargs)
        if len(args) + len(kwargs) == 3:
            return Triangle(*args, **kwargs)
        raise ValueError('Передано неверное количество аргументов')