from math import factorial


def factorial_division(number_1, number_2):
    fact_1 = factorial(number_1)
    fact_2 = factorial(number_2)
    result = fact_1 / fact_2
    print(f"{result:.2f}")
    return result


factorial_division(int(input()), int(input()))
