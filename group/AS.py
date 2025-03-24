def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

# Example usage
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

print("Result:", divide(num1, num2))
