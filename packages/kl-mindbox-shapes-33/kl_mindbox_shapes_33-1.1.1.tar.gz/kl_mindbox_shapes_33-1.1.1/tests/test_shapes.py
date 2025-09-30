import unittest
import math

from kl_mindbox_shapes_33 import AutoShape
from kl_mindbox_shapes_33.triangle import (
    AutoTriangle,
    Triangle,
    RightAngleTriangle,
    IsoscelesTriangle,
    IsoscelesRightTriangle,
)
from kl_mindbox_shapes_33.circle import Circle

class TestShapes(unittest.TestCase):
    def test_triangle_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0)

    def test_right_angle_triangle(self):
        r = RightAngleTriangle(5, 3, 4)
        self.assertAlmostEqual(r.area(), 6.0)
        self.assertAlmostEqual(r.perimeter(), 12.0)

    def test_isosceles_triangle(self):
        iso = IsoscelesTriangle(4, 5)
        height = math.sqrt(5**2 - (4/2)**2)
        expected_area = (4 * height) / 2
        self.assertAlmostEqual(iso.area(), expected_area)

    def test_isosceles_right_triangle(self):
        ir = IsoscelesRightTriangle(3)
        self.assertAlmostEqual(ir.area(), 4.5)
        self.assertAlmostEqual(ir.perimeter(), 3 + 3 + 3*math.sqrt(2))

    def test_circle(self):
        c = Circle(2)
        self.assertAlmostEqual(c.area(), math.pi * 4)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 2)

    def test_auto_triangle(self):
        t = AutoTriangle.create(3, 4, 5)
        self.assertIsInstance(t, RightAngleTriangle)
        t2 = AutoTriangle.create(5, 5, 6)
        self.assertIsInstance(t2, IsoscelesTriangle)

    def test_auto_shape_circle(self):
        c = AutoShape.create([2])
        self.assertIsInstance(c, Circle)
        self.assertAlmostEqual(c.area(), math.pi * 4)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 2)

    def test_auto_shape_triangle_right(self):
        t = AutoShape.create([3, 4, 5])
        self.assertIsInstance(t, RightAngleTriangle)
        self.assertAlmostEqual(t.area(), 6.0)
        self.assertAlmostEqual(t.perimeter(), 12.0)

    def test_auto_shape_triangle_isosceles(self):
        t = AutoShape.create([5, 5, 6])
        self.assertIsInstance(t, IsoscelesTriangle)
        height = math.sqrt(5**2 - (6/2)**2)
        expected_area = (6 * height)/2
        self.assertAlmostEqual(t.area(), expected_area)

    def test_auto_shape_invalid(self):
        with self.assertRaises(ValueError):
            AutoShape.create([])
        with self.assertRaises(ValueError):
            AutoShape.create([1, 2])  

if __name__ == "__main__":
    unittest.main()    
