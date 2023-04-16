sequence_of_numbers = [int(x) for x in input().split(', ')]
for group in range(10, max(sequence_of_numbers) + 10, 10):
    print(f"Group of {group}'s: {[x for x in sequence_of_numbers if group - 10 < x <= group]}")
