def line_length(point_x: float, point_y: float):
    from math import sqrt
    length = sqrt(pow(point_x, 2) + pow(point_y, 2))
    return length


def closest_to_center(x1: float, y1: float, x2: float, y2: float):
    from math import floor
    line_1 = line_length(x1, y1)
    line_2 = line_length(x2, y2)
    if line_1 <= line_2:
        print(f"({floor(x1)}, {floor(y1)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})")


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

closest_to_center(x_1, y_1, x_2, y_2)
