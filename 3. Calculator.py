class Calculator:

    def add(self, a: float, b: float, round_otput=3):
        return round(a + b, round_otput)

    def subtract(self, a: float, b: float, round_otput=3):
        return round(a - b, round_otput)

    def multiply(self, a: float, b: float, round_otput=3):
        return round(a * b, round_otput)

    def divide(self, a: float, b: float, round_otput=3):
        if b == 0:
            raise ValueError("b cannot be zero")
        return round(a / b, round_otput)

def main():
    calculator = Calculator()
    print(calculator.add(5.34567, 2.2121121))
    print(calculator.subtract(12,7.5))
    print(calculator.multiply(6,6))
    print(calculator.divide(6,1))

if __name__ == "__main__":
    main()
