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
        self._a = a
        self._b = b
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
        self.area = self.determine_area()
        self.perimeter = self.determine_perimeter()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b: float):
        if b <= 0:
            raise ValueError("b must be greater than zero")
        self._b = b
        self.area = self.determine_area()
        self.perimeter = self.determine_perimeter()

    def determine_area(self, otput_round=3) -> float:
        return round(self.a * self.b, otput_round)

    def determine_perimeter(self, otput_round=3) -> float:
        return round(2 * self.a + 2 * self.b, otput_round)


class Triangle(Shape):

    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c
        self.valid_triangle()
        self.s = self.determine_s()
        self.perimeter = self.determine_perimeter()
        self.area = self.determine_area()

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a: float):
        if a <= 0:
            raise ValueError("a must be greater than zero")
        self.valid_triangle()
        self._a = a
        self.perimeter = self.determine_perimeter()
        self.area = self.determine_area()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b: float):
        if b <= 0:
            raise ValueError("b must be greater than zero")
        self.valid_triangle()
        self._b = b
        self.perimeter = self.determine_perimeter()
        self.area = self.determine_area()

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c: float):
        if c <= 0:
            raise ValueError("c must be greater than zero")
        self.valid_triangle()
        self._c = c
        self.perimeter = self.determine_perimeter()
        self.area = self.determine_area()

    def determine_s(self) -> float:
        return (self.a + self.b + self.c) / 2

    def determine_perimeter(self, otput_round=3) -> float:
        return round(self.a + self.b + self.c, otput_round)

    def determine_area(self, otput_round=3) -> float:
        s = self.determine_s()
        return round(math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)), otput_round)

    def valid_triangle(self) -> bool:
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.b + self.a:
            return True
        raise ValueError("The sum of two side lengths has to exceed the length of the third side!")

def main():
    C = Circle(3)
    print(C.radius, C.perimeter, C.area)
    C.radius = 3.5
    print(C.radius, C.perimeter, C.area, "\n")

    B = Rectangle(5.5, 8.2)
    print(B.a, B.b, B.perimeter, B.area)
    B.a = 6
    print(B.a, B.b, B.perimeter, B.area, "\n")

    A = Triangle(4, 3, 2)
    print(A.a, A.b, A.c, A.perimeter, A.area)
    A.a = 4.3
    print(A.a, A.b, A.c, A.perimeter, A.area)

if __name__ == "__main__":
    main()
