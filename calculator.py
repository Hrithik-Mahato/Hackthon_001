def calculator(num1, num2, operation):
    """Performs basic arithmetic operations: addition, subtraction, multiplication, and division."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'
    else:
        return 'Error: Invalid operation'

# Example usage:
print(calculator(10, 5, '+'))  # 15
print(calculator(10, 5, '-'))  # 5
print(calculator(10, 5, '*'))  # 50
print(calculator(10, 5, '/'))  # 2.0
print(calculator(10, 0, '/'))  # Error: Division by zero
