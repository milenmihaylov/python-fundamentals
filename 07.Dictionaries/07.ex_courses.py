courses = {}

command = input()
while not command == 'end':
    course_name, student_name = command.split(' : ')
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

for course, students_list in sorted(courses.items(), key=lambda x: -len(x[1])):
    print(f"{course}: {len(students_list)}")
    students_list.sort()
    for student in students_list:
        print(f"-- {student}")
