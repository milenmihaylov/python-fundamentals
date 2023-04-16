# да се опитам отново

string = input().split()
k = int(input())
the_list_itself = [int(x) for x in string]

josephus_permutation = []
count = 0
index = 0
# 1ви index += k


while the_list_itself:
    count += 1
    if index == len(the_list_itself):
        index = 0
        # count -= len(the_list_itself)
    if count % k == 0:
        josephus_permutation.append(the_list_itself.pop(index))
        index -= 1
    index += 1

print(str(josephus_permutation).replace(' ', ''))
