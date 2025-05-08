class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

def main():
    cal = Calculator(6, 5)
    print(cal.add())
    print(cal.sub())
    print(cal.mul())
    print(cal.div())

if __name__ == "__main__":
    main()
