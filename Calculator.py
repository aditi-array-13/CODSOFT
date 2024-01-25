# CodSoft
# Task 2
# Calculator

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."


def exponent(x, y):
    return x ** y


def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot perform modulo by zero."


def floor_divide(x, y):
    if y != 0:
        return x // y
    else:
        return "Cannot perform floor division by zero."


def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (**)")
    print("6. Modulo (%)")
    print("7. Floor Division (//)")

    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (1-7): ")

    # Perform calculation based on user's choice
    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)
    elif operation == '5':
        result = exponent(num1, num2)
    elif operation == '6':
        result = modulo(num1, num2)
    elif operation == '7':
        result = floor_divide(num1, num2)
    else:
        result = "Invalid operation."

    # Display the result
    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()