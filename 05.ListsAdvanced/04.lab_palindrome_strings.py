palindromes = [el for el in input().split() if el == el[::-1]]
word = input()
print(palindromes)
print(f"Found palindrome {palindromes.count(word)} times")

nums = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, nums)))
