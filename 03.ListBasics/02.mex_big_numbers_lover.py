# logic: https://www.geeksforgeeks.org/arrange-given-numbers-form-biggest-number-set-2/
# да се опитам отново


numbers_list = input().split()
numbers_int = [int(x) for x in numbers_list]

l = len(str(max(numbers_int))) + 1
extended_values = []
ans = ''

for i in numbers_int:
    temp = str(i) * l
    extended_values.append((temp[:l:], i))
    extended_values.sort(reverse=True)

for i in extended_values:
    ans += str(i[1])

print(int(ans))
