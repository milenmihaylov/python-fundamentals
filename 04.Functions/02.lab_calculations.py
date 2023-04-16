def calculations(operator, a, b):
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    else:
        result = None
    return int(result)


operation = input()
num_1 = int(input())
num_2 = int(input())

print(calculations(operation, num_1, num_2))
