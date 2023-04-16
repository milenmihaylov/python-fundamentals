from string import ascii_lowercase

info = input()
students = {}
while info[0] not in ascii_lowercase:
    name, stud_id, course = info.split(':')
    if course not in students:
        students[course] = {}
    students[course].update({name: stud_id})
    info = input()

if '_' in info:
    info = info.replace('_', ' ')

for name, stud_id in students[info].items():
    print(f"{name} - {stud_id}")
