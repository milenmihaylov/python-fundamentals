n = int(input())
positive_num_list = []
negative_num_list = []
for i in range(n):
    number = int(input())
    if number >= 0:
        positive_num_list.append(number)
    else:
        negative_num_list.append(number)

count_positives = len(positive_num_list)
sum_of_negatives = sum(negative_num_list)

print(positive_num_list)
print(negative_num_list)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}")
