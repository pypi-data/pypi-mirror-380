from typing import List
from .base import Shape
from .triangle import AutoTriangle
from .circle import Circle
class AutoShape:    
    @classmethod
    def create(cls, sides: List[float]) -> Shape:
        n = len(sides)
        if n == 0:
            raise ValueError('Shape must have at least one side')        
        if n == 1:
            # it's circle
            return Circle(sides[0])
        if n == 3:
            # it's triangle
            return AutoTriangle.create(*sides)
        raise ValueError("We don't know such figure at yet")