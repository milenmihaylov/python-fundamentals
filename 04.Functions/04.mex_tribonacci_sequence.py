nums = int(input())
num_1 = 0
num_2 = 0
num_3 = 0
number = 1
print(1, end=' ')
for i in range(nums - 1):
    num_3 = num_2
    num_2 = num_1
    num_1 = number
    number = num_1 + num_2 + num_3
    print(number, end=' ')
