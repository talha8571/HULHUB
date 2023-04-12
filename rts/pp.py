class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


calc = Calculator()

# Overloaded method with two parameters
print(calc.add(2, 3))  # Output: 5

# Overloaded method with three parameters
# print(calc.add(2, 3, 4))  # Output: 9