# Simple Calculator using a class

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        else:
            return x / y

calc = Calculator()

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"{num1} + {num2} = {calc.add(num1, num2)}")

elif choice == '2':
    print(f"{num1} - {num2} = {calc.subtract(num1, num2)}")

elif choice == '3':
    print(f"{num1} * {num2} = {calc.multiply(num1, num2)}")

elif choice == '4':
    print(f"{num1} / {num2} = {calc.divide(num1, num2)}")

else:
    print("Invalid input")