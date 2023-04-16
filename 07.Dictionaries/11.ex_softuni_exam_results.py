exam_results = {}
submissions = {}
information = input()
while not information == 'exam finished':
    information = information.split('-')
    if len(information) > 2:
        username, language, points = information
        if username not in exam_results:
            exam_results[username] = 0
        if exam_results[username] < int(points):
            exam_results[username] = int(points)

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

    elif information[1] == 'banned':
        username = information[0]
        exam_results.pop(username)

    information = input()

print('Results:')
for username, points in sorted(exam_results.items(), key=lambda x: (-x[1], x[0])):
    print(f"{username} | {points}")

print('Submissions:')
for language, total_submissions in sorted(submissions.items(), key=lambda x: (-x[1], x[0])):
    print(f'{language} - {total_submissions}')
