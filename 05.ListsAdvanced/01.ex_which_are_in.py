first_string = input().split(', ')
second_string = input()

print([x for x in first_string if x in second_string])
