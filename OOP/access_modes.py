#from accessify import private, protected - can use these decorators for much stronger protection
from typing import Any
class Point:
    def __init__(self, x: Any[int, float] = 0, y: Any[int, float] = 0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls, x: Any[int, float]):
        return isinstance(x, Any[int, float])

    def set_coords(self, x: Any[int, float], y: Any[int, float]):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Type mismatch")


    def get_coords(self):
        return self.__x, self.__y


