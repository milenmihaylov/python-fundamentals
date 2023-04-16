# numbers = list(map(int, input().split(', ')))
# print(f"Positive: {', '.join([str(num) for num in numbers if num >= 0])}")
# print(f"Negative: {', '.join([str(num) for num in numbers if num < 0])}")
# print(f"Even: {', '.join([str(num) for num in numbers if num % 2 == 0])}")
# print(f"Odd: {', '.join([str(num) for num in numbers if not num % 2 == 0])}")

numbers = [int(x) for x in input().split(', ')]

positives, negatives, even, odd = [], [], [], []
for num in numbers:
    positives.append(str(num)) if num >= 0 else negatives.append(str(num))
    even.append(str(num)) if num % 2 == 0 else odd.append(str(num))

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
