import pytest
import math
from area_calc import Circle, Triangle

def test_circle_area():
    c = Circle(5)
    assert c.area() == math.pi * 25

def test_triangle_area():
    t = Triangle(5, 6, 7)
    perm = (5 + 6 + 7) / 2
    result = perm * (perm - 5) * (perm - 6) * (perm - 7)
    assert t.area() == math.sqrt(result)    

def test_triangle_is_angled():
    t = Triangle(3, 4, 5)
    assert t.is_right_angled() is True

def test_triangle_is_not_angle():
    t = Triangle(5, 6, 7)
    assert t.is_right_angled() is False    

def test_triangle_validation_fails():
    with pytest.raises(ValueError):
        Triangle(1, 1, 10)    
