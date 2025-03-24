from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        operation = input("Select operation (+, -, *, /): ").strip()

        result = None
        if operation == "+":
            result = Addition.add(num1, num2)
        elif operation == "-":
            result = Subtraction.subtract(num1, num2)
        elif operation == "*":
            result = Multiplication.multiply(num1, num2)
        elif operation == "/":
            result = Division.divide(num1, num2)
        else:
            print("Invalid operation selected.")
        
        if result is not None:
            print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
