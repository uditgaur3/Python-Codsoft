import math
def subtract(p, q):
    return p - q
def add(p, q):
    return p + q
def multiply(p, q):
    return p * q
def divide(p, q):
    if q != 0:
        return p / q
    else:
        return "Error\n"

def power(p, q):
    return p ** q

def logarithm(p, base):
    return math.log(p, base)

def square_root(p):
    return math.sqrt(p)

def sin(p):
    return math.sin(math.radians(p))

def cos(p):
    return math.cos(math.radians(p))

def tan(p):
    return math.tan(math.radians(p))

def scientific_calculator():
    print("-------Calculator-------")
    print("choose any one:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Logarithm")
    print("7. Square Root")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")

    choice = input("Enter choice (1-10): ")

    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print("Invalid input")
        return

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    else:
        num1 = float(input("Enter a number: "))

    if choice == '1':
        result = add(num1, num2)
        operator = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operator = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operator = "*"
    elif choice == '4':
        result = divide(num1, num2)
        operator = "/"
    elif choice == '5':
        result = power(num1, num2)
        operator = "^"
    elif choice == '6':
        base = float(input("Enter the base for the logarithm: "))
        result = logarithm(num1, base)
        operator = "log"
    elif choice == '7':
        result = square_root(num1)
        operator = "sqrt"
    elif choice == '8':
        result = sin(num1)
        operator = "sin"
    elif choice == '9':
        result = cos(num1)
        operator = "cos"
    elif choice == '10':
        result = tan(num1)
        operator = "tan"

    if isinstance(result, float):
        print(f"{operator}({num1}) = {result:.4f}")
    else:
        print(result)

if __name__ == "__main__":
    scientific_calculator()
