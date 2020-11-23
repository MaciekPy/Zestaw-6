# W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami.
# Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych,
#  o końcu w położeniu (x, y). Napisać kod testujący moduł points.

import unittest
import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):       # zwraca string "(x, y)"
        print("({}, {})".format(self.x, self.y))

    def __repr__(self):    # zwraca string "Point(x, y)"
        print("Point({}, {})".format(self.x, self.y))

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return (self.x != other.x) and (self.y != other.y)

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __sub__(self, other):  # v1 - v2
        self.x = self.x - other.x
        self.y = self.y - other.y
        return self

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(self.x**2 + self.y**2)
        # Kod testujący moduł.


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.point1 = Point(3, 4)
        self.point2 = Point(1, 2)

    def test_eq(self):
        self.assertEqual(self.point1.__eq__(self.point2), False)

    def test_ne(self):
        self.assertEqual(self.point1.__ne__(self.point2), True)

    def test_add(self):
        self.assertEqual(self.point1.__add__(self.point2), Point(4, 6))

    def test_sub(self):
        self.assertEqual(self.point1.__sub__(self.point2), Point(2, 2))

    def test_mul(self):
        self.assertEqual(self.point1.__mul__(self.point2), 11)

    def test_cross(self):
        self.assertEqual(self.point1.cross(self.point2), 2)

    def test_length(self):
        self.assertEqual(self.point1.length(), 5)


if __name__ == "__main__":
    unittest.main()  # uruchamia wszystkie testy
