from statistics import mean

employees_happiness = input().split()
happiness_improvement_factor = int(input())

# List comprehension:
employees_happiness = [int(x) * happiness_improvement_factor for x in employees_happiness]
happy_count = len([x for x in employees_happiness if x >= mean(employees_happiness)])
total_count = len(employees_happiness)

# map() and filter():
# employees_happiness = list(map(lambda x: int(x)*happiness_improvement_factor, employees_happiness))
# happy_count = len(list(filter(lambda x: x >= mean(employees_happiness), employees_happiness)))
# total_count = len(employees_happiness)

if happy_count >= total_count * 0.5:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
