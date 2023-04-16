def exchange(list_of_numbers, i):
    return list_of_numbers[i + 1:] + list_of_numbers[:i + 1]


def max_even(list_of_numbers):
    even_numbers = [num for num in list_of_numbers if num % 2 == 0]
    if len(even_numbers) > 0:
        max_number = max(even_numbers)
        max_number_index = None
        for i in range(len(list_of_numbers)):
            if list_of_numbers[i] == max_number:
                max_number_index = i
        return max_number_index
    else:
        return "No matches"


def max_odd(list_of_numbers):
    odd_numbers = [num for num in list_of_numbers if not num % 2 == 0]
    if len(odd_numbers) > 0:
        max_number = max(odd_numbers)
        max_number_index = None
        for i in range(len(list_of_numbers)):
            if list_of_numbers[i] == max_number:
                max_number_index = i
        return max_number_index
    else:
        return "No matches"


def min_even(list_of_numbers):
    even_list = [num for num in list_of_numbers if num % 2 == 0]
    if len(even_list) > 0:
        min_number = min(even_list)
        min_number_index = None
        for i in range(len(list_of_numbers)):
            if list_of_numbers[i] == min_number:
                min_number_index = i
        return min_number_index
    else:
        return "No matches"


def min_odd(list_of_numbers):
    odd_list = [num for num in list_of_numbers if not num % 2 == 0]
    if len(odd_list) > 0:
        min_number = min(odd_list)
        min_number_index = None
        for i in range(len(list_of_numbers)):
            if list_of_numbers[i] == min_number:
                min_number_index = i
        return min_number_index
    else:
        return "No matches"


def first_even(list_of_numbers, cnt):
    first_last_list = [num for num in list_of_numbers if num % 2 == 0]
    return first_last_list[:cnt]


def first_odd(list_of_numbers, cnt):
    first_last_list = [num for num in list_of_numbers if not num % 2 == 0]
    return first_last_list[:cnt]


def last_even(list_of_numbers, cnt):
    first_last_list = [num for num in list_of_numbers if num % 2 == 0]
    return first_last_list[-cnt:]


def last_odd(list_of_numbers, cnt):
    first_last_list = [num for num in list_of_numbers if not num % 2 == 0]
    return first_last_list[-cnt:]


num_list = [int(x) for x in input().split()]
manipulation_command = input().split()
command = manipulation_command[0]

while not command == 'end':
    if command == 'exchange':
        index = int(manipulation_command[1])
        if index in range(len(num_list)):
            num_list = exchange(num_list, index)
        else:
            print("Invalid index")

    elif command == 'max':
        if manipulation_command[1] == 'even':
            print(max_even(num_list))
        elif manipulation_command[1] == 'odd':
            print(max_odd(num_list))

    elif command == 'min':
        if manipulation_command[1] == 'even':
            print(min_even(num_list))
        elif manipulation_command[1] == 'odd':
            print(min_odd(num_list))

    elif command == 'first':
        count = int(manipulation_command[1])
        if count > len(num_list):
            print("Invalid count")
        elif manipulation_command[2] == 'even':
            print(first_even(num_list, count))
        elif manipulation_command[2] == 'odd':
            print(first_odd(num_list, count))

    elif command == 'last':
        count = int(manipulation_command[1])
        if count > len(num_list):
            print("Invalid count")
        elif manipulation_command[2] == 'even':
            print(last_even(num_list, count))
        elif manipulation_command[2] == 'odd':
            print(last_odd(num_list, count))

    manipulation_command = input().split()
    command = manipulation_command[0]

else:
    print(num_list)
