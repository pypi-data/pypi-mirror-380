from .base import Shape
import math
"""
AutoTriangle class automatically defines typ of triangle by its inner checking methods and returns it,
you may to add some logic like isosceles, equilateral triangle etc
"""
class AutoTriangle:        
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        pass
    @classmethod
    def create(cls, a:float, b: float, c: float) -> Shape:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Sides cant be 0 or negative')
        if a + b <= c or b + c <= a or a + c <= b: 
            raise ValueError('Triangle is invalid')
        obj = cls(a, b, c)             
        is_right_angle = obj._check_on_right_angle()
        is_isosceles = obj._check_on_isosceles()

        if is_right_angle and is_isosceles:
            return IsoscelesRightTriangle(obj.b)
        if is_right_angle:
            return RightAngleTriangle(obj.hypotenuse, obj.catet1, obj.catet2)
        if is_isosceles:
            return IsoscelesTriangle(obj.base, obj.side)
        return Triangle(a, b, c)
    
    def _check_on_right_angle(self) -> bool:
        a_sq = self.a **2
        b_sq = self.b ** 2
        c_sq = self.c ** 2
        if a_sq == b_sq + c_sq:
            self.hypotenuse = self.a
            self.catet1 = self.b
            self.catet2 = self.c
            return True
        if b_sq == a_sq + c_sq:
            self.hypotenuse = self.b
            self.catet1 = self.a
            self.catet2 = self.c
            return True
        if c_sq == b_sq + a_sq:
            self.hypotenuse = self.c
            self.catet1 = self.a
            self.catet2 = self.b
            return True
        return False
    def _check_on_isosceles(self) -> bool:
        if self.a == self.b:
            self.base = self.c
            self.side = self.a
            return True       
        if self.a == self.c:
            self.base = self.b
            self.side = self.a
            return True        
        if self.b == self.c:
            self.base = self.a
            self.side = self.b
            return True       
        return False

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c  
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(
            p * (p - self.a) * (p - self.b) * (p - self.c)
        )
    def perimeter(self):
        return self.a + self.b + self.c

class RightAngleTriangle(Shape):
    def __init__(self, hypotenuse: float, catet1: float, catet2: float):
        super().__init__()
        self.hypotenuse = hypotenuse
        self.catet1 = catet1
        self.catet2 = catet2
    def area(self):
        return (self.catet1 * self.catet2 ) / 2
    def perimeter(self):
        return self.hypotenuse + self.catet1 + self.catet2
class IsoscelesTriangle(Shape):
    def __init__(self, base : float, side: float):
        super().__init__()
        self.base = base
        self.side = side
    def area(self):     
        height = math.sqrt(self.side ** 2 - (self.base / 2) ** 2)
        return (self.base * height) / 2

    def perimeter(self):
        return self.base + 2 * self.side
    
class IsoscelesRightTriangle(Shape):
    def __init__(self, catet: float):
        self.catet = catet
        self.hypotenuse = math.sqrt(2) * catet

    def area(self) -> float:
        return (self.catet ** 2) / 2

    def perimeter(self) -> float:
        return 2 * self.catet + self.hypotenuse
