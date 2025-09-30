from .base import Shape
import math
class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()  
        if radius <= 0:
            raise ValueError('radius cant be 0 or negative')                  
        self.radius = radius                
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
    