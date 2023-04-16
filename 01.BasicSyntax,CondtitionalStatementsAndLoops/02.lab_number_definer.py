number = float(input())

if abs(number) < 1 and not number == 0:
    print("small", end=' ')
elif abs(number) > 1000000:
    print("large", end=' ')


if number == 0:
    print("zero")
elif number > 0:
    print("positive")
else:
    print("negative")

