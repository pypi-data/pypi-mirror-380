from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int | float):
        if not radius > 0:
            raise ValueError('Радиус не может быть меньше или равным нулю')
        self.radius: int | float = radius

    def area(self) -> float:
        circle_area = self.radius ** 2 * math.pi
        return circle_area
    

class Triangle(Shape):
    def __init__(self, a: int | float, b: int | float , c: int | float):
            if not (a + b > c and a + c > b and b + c > a):
                raise ValueError('Треугольник с такими сторонами не может существовать')
            self.a: int | float = a
            self.b: int | float = b
            self.c: int | float = c

    def _get_half_perimetr(self):
        perm = (self.a + self.b + self.c) / 2
        return perm

    def _difference_between_perm_and_sides(self):
        half_perm = self._get_half_perimetr()
        result_for_A = half_perm - self.a
        result_for_B = half_perm - self.b
        result_for_C = half_perm - self.c
        result = half_perm * (result_for_A) * (result_for_B) * (result_for_C)
        return result
    
    def area(self) -> float:
        s = self._difference_between_perm_and_sides()
        triangle_area = math.sqrt(s)    
        return triangle_area
    
    def is_right_angled(self, tolerance = 1e-9):
        sides = sorted([self.a, self.b, self.c])
        a, b, c = sides[0], sides[1], sides[2]
        return abs(a ** 2 + b ** 2 - c ** 2) < tolerance
    

def calculate_shape_area(shape_obj):
    if isinstance(shape_obj, Shape):
        return shape_obj.area()
    raise TypeError('Объект должен быть экземпляром класса Shape')
