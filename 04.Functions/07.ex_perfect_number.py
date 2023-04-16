def perfect_number(number):
    num_list = []
    for i in range(number - 1, 0, -1):
        if number % i == 0:
            num_list.append(i)

    if sum(num_list) == number:
        result = "We have a perfect number!"
    else:
        result = "It's not so perfect."

    print(result)
    return result


perfect_number(int(input()))
