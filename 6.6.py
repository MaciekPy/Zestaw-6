import unittest


class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        self.size = n + 1       # rozmiar tablicy
        self.a = self.size * [0]
        self.a[self.size-1] = c

    def __str__(self):
        return str(self.a)

    def __add__(self, other):  # poly1 + poly2
        poly3 = self.a

        for i in range(other.size):
            if i < len(poly3):
                poly3[i] = poly3[i] + other.a[i]
            else:
                poly3.append(other.a[i-1])

        polyWynik = Poly(0, len(poly3))
        polyWynik.a = poly3

        return polyWynik

    def __sub__(self, other):  # poly1 - poly2
        poly3 = self.a

        for i in range(other.size):
            if i < len(poly3):
                poly3[i] = poly3[i] - other.a[i]
            else:
                poly3.append(-other.a[i])
        polyWynik = Poly(0, len(poly3))
        polyWynik.a = poly3
        return polyWynik

    def __mul__(self, other):  # poly1 * poly2
        poly3 = Poly(0, self.size + other.size)

        for i in range(self.size):
            for j in range(other.size):
                poly3.a[i + j] = poly3.a[i + j] + (self.a[i] * other.a[j])

        return poly3

    def __pos__(self):         # +poly1 = (+1)*poly1
        for i in range(self.size):
            self.a[i] = +1 * self.a[i]
        return self

    def __neg__(self):         # -poly1 = (-1)*poly1
        for i in range(self.size):
            self.a[i] = -1 * self.a[i]
        return self

    def __ne__(self, other):        # obsługa poly1 != poly2
        if self.size != other.size:
            return True

        for i in range(self.size):
            if self.a[i] != other.a[i]:
                return True

        return False

    def eval(self, x):       # schemat Hornera
        self.a.reverse()
        result = self.a[0]

        for i in range(1, self.size):

            result = result * x + self.a[i]

        return result

    def __eq__(self, other):       # obsługa poly1 == poly2
        if self.size != other.size:
            return False

        for i in range(self.size):
            if self.a[i] != other.a[i]:
                return False

        return True

    def __pow__(self, n):      # poly(x)**n lub pow(poly(x),n)
        poly2 = self
        if n == 2:
            poly2 = self.__mul__(self)
        elif n > 2:
            for _ in range(n-1):
                poly2 = self.__mul__(poly2)

        return poly2

    def combine(self, other):     # złożenie poly1(poly2(x))
        poly3 = Poly(0, 0)

        for i in range(1, self.size):
            poly4 = Poly(0, 0)
            poly4 = other.__pow__(i)
            poly5 = Poly(0, poly4.size)
            poly5.a = [j * self.a[i] for j in poly4.a]
            poly3 = poly3.__add__(poly5)

        return poly3

    def diff(self):            # różniczkowanie
        poly = self

        for i in range(1, self.size):
            poly.a[i-1] = self.a[i] * i
        poly.a[self.size - 1] = 0

        return poly

    def integrate(self):      # całkowanie
        poly = Poly(0, self.size)

        for i in range(1, self.size+1):
            poly.a[i] = self.a[i-1] * (i-1)

        return poly

    def is_zero(self):        # bool, True dla [0], [0, 0],...
        for i in range(self.size):
            if self.a[i] != 0:
                return False
        return True


# Kod testujący moduł.


class TestPoly(unittest.TestCase):

    def setUp(self):
        self.poly1 = Poly(4, 3)
        self.poly2 = Poly(2, 2)

    def test_add(self):
        self.assertEqual(self.poly1.__add__(self.poly2).a, [0, 0, 2, 4])

    def test_sub(self):
        self.assertEqual(self.poly1.__sub__(self.poly2).a, [0, 0, -2, 4])

    def test_mul(self):
        self.assertEqual(self.poly1.__mul__(
            self.poly2).a, [0, 0, 0, 0, 0, 8, 0, 0])

    def test_ne(self):
        self.assertEqual(self.poly1.__ne__(self.poly2), True)

    def test_eval(self):
        self.assertEqual(self.poly1.eval(2), 32)

    def test_eq(self):
        self.assertEqual(self.poly1.__eq__(self.poly2), False)

    def test_combine(self):
        self.assertEqual(self.poly1.combine(self.poly2).a,
                         [0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0])

    def test_is_zero(self):
        self.assertEqual(self.poly1.is_zero(), False)

    def test_pos(self):
        self.assertEqual(self.poly1.__pos__().a, [0, 0, 0, 4])

    def test_neg(self):
        self.assertEqual(self.poly1.__neg__().a, [0, 0, 0, -4])

    def test_diff(self):
        self.assertEqual(self.poly1.diff().a, [0, 0, 12, 0])

    def test_integrate(self):
        self.assertEqual(self.poly1.integrate().a, [0, 0, 0, 0, 12])


if __name__ == "__main__":
    unittest.main()  # uruchamia wszystkie testy
