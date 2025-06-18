import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_print(c, d, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        c_decimal, d_decimal = map(Decimal, [c, d])
        result = operation_mappings.get(operation_name)
        if result:
            print(f"The result of {c} {operation_name} {d} is equal to {result(c_decimal, d_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {c} or {d} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, c, d, operation = sys.argv
    calculate_and_print(c, d, operation)

if __name__ == '__main__':
    main()
