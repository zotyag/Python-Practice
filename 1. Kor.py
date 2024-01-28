import math

class Circle:
    def __init__(self, radius:float):
        self.radius=radius

    def kerulet(self):
        return 2*self.radius*math.pi

    def terulet(self):
        return self.radius*self.radius*math.pi


def main():
    kor1=Circle(4)
    print(kor1.kerulet())
    print(kor1.terulet())

if __name__ == '__main__':
    main()
