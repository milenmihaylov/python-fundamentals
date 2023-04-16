def sum_numbers(num_1: int, num_2: int):
    sum_result = num_1 + num_2
    return sum_result


def subtract(sum_number, num_3):
    subtract_result = sum_number - num_3
    return subtract_result


def add_and_subtract():
    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())
    sum_numbers(number_1, number_2)
    print(subtract(sum_numbers(number_1, number_2), number_3))


add_and_subtract()
