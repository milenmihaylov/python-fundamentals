def line_length(point1: tuple = (0, 0), point2: tuple = (0, 0)):
    from math import sqrt
    (x1, y1) = point1
    (x2, y2) = point2
    length = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    return length


def closer_to_center(point1: tuple, point2: tuple):
    from math import floor
    (x1, y1) = point1
    (x2, y2) = point2
    line_1 = line_length(point1)
    line_2 = line_length(point2)

    if line_1 <= line_2:
        print(f"({floor(x1)}, {floor(y1)})", end='')
        print(f"({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})", end='')
        print(f"({floor(x1)}, {floor(y1)})")


point_1 = (float(input()), float(input()))
point_2 = (float(input()), float(input()))
point_3 = (float(input()), float(input()))
point_4 = (float(input()), float(input()))

length_line_1 = line_length(point_1, point_2)
length_line_2 = line_length(point_3, point_4)

if length_line_1 >= length_line_2:
    closer_to_center(point_1, point_2)
else:
    closer_to_center(point_3, point_4)
