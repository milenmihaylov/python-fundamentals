from statistics import mean
students = {}

for _ in range(int(input())):
    student_name = input()
    student_grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

for student_name, grades_list in students.items():
    ave_grade = mean(grades_list)
    students[student_name] = float(ave_grade)


for student_name, ave_grade in sorted(students.items(), key=lambda x: -x[1]):
    if ave_grade >= 4.5:
        print(f"{student_name} -> {ave_grade:.2f}")
    else:
        break

