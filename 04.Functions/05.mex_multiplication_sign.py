def product_sign(number_1: float, number_2: float, number_3: float):
    negatives = 0
    for number in (number_1, number_2, number_3):
        if number < 0:
            negatives += 1
        elif number == 0:
            print('zero')
            exit()
    if negatives % 2 == 0:
        print('positive')
    else:
        print('negative')


num_1 = float(input())
num_2 = float(input())
num_3 = float(input())

product_sign(num_1, num_2, num_3)
