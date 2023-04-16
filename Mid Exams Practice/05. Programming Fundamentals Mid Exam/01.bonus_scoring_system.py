from math import ceil

students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())

student_attendances = []
for attendances in range(students_count):
    student_attendances.append(int(input()))
if len(student_attendances) > 0 :
    max_attendances = max(student_attendances)
else:
    max_attendances = 0
if not lectures_count == 0:
    total_bonus = (max_attendances / lectures_count) * (5 + initial_bonus)
else:
    total_bonus = 0

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")
