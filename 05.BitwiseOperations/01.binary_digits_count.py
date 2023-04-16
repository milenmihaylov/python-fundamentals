n_d = int(input())
b = input()

count = 0
# n_b = bin(n_d)
# for el in n_b[2:]:
#     if el == b:
#         count += 1
while n_d > 1:
    if n_d % 2 == int(b):
        count += 1
    n_d //= 2

print(count)
