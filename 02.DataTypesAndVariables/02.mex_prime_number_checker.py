number = int(input())
prime = True
if number > 2 and not number % 2 == 0:
    for i in range(3, int(number/2 + 1)):
        if number % i == 0:
            prime = False
            break

elif number == 2:
    prime = True

else:
    prime = False

print(prime)
