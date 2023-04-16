employees_efficiency = [int(input()) for x in range(3)]
people_to_answer = int(input())

total_efficiency = sum(employees_efficiency)
time_needed = 0
break_time = 0
while people_to_answer > 0:
    time_needed += 1
    people_to_answer -= total_efficiency
    break_time += 1
    if break_time == 3 and people_to_answer > 0:
        time_needed += 1
        break_time = 0


print(f"Time needed: {time_needed}h.")
