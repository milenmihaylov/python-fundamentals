pattern = int(input())

for i in range(1, pattern + 1):
    print('*' * i)

for j in range(pattern - 1, 0, -1):
    print('*' * j)
