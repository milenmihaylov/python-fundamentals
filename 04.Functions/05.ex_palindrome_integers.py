def palindrome():
    numbers = input().split(', ')
    for number in numbers:
        is_palindrome = False
        for i in range(len(number)):
            if not number[i] == number[-(i + 1)]:
                is_palindrome = False
                break
            else:
                is_palindrome = True

        print(is_palindrome)


palindrome()
