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


def main():
    c = Circle(3)
    print(c.radius, c.perimeter, c.area)


if __name__ == "__main__":
    main()
