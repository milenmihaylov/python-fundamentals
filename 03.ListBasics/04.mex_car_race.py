input_times = input().split()
times_list = [int(x) for x in input_times]

time_left_car = 0
time_right_car = 0

left_car = times_list[:(len(times_list) // 2)]
right_car = times_list[(len(times_list) // 2) + 1:]

for l_time in range(len(left_car)):
    time_left_car += left_car[l_time]
    if left_car[l_time] == 0:
        time_left_car *= 0.8

for r_time in range(len(right_car) - 1, -1, -1):
    time_right_car += right_car[r_time]
    if right_car[r_time] == 0:
        time_right_car *= 0.8

if time_left_car < time_right_car:
    print(f"The winner is left with total time: {time_left_car:.1f}")
else:
    print(f"The winner is right with total time: {time_right_car:.1f}")
