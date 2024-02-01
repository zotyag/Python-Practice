import math


class Shape:

    def area(self):
        ...

    def perimeter(self):
        ...


class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius
        self.perimeter = self.determine_perimeter()
        self.area = self.determine_area()

    def __str__(self):
        return f"It is a circle wth a radius of {self.radius}"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be greater than zero")
        self._radius = radius
        self.perimeter = self.determine_perimeter()
        self.area = self.determine_area()

    def determine_perimeter(self, otput_round=3) -> float:
        return round(2 * math.pi * self.radius, otput_round)

    def determine_area(self, otput_round=3) -> float:
        return round(math.pi * (self.radius ** 2), otput_round)


class Rectangle(Shape):

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        self.area = self.determine_area()
        self.perimeter = self.determine_perimeter()

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a: float):
        if a <= 0:
            raise ValueError("a must be greater than zero")
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b: float):
        if b <= 0:
            raise ValueError("b must be greater than zero")
        self._b = b

    def determine_area(self, otput_round=3) -> float:
        return round(self.a * self.b, otput_round)

    def determine_perimeter(self, otput_round=3) -> float:
        return round(2 * self.a + 2 * self.b, otput_round)


def main():
    C = Circle(3)
    print(C.radius, C.perimeter, C.area)

    B = Rectangle(5.5, 8.2)
    print(B.a, B.b, B.area, B.perimeter)


if __name__ == "__main__":
    main()
