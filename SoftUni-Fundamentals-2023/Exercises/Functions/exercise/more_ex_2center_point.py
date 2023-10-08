from math import *
def center_point(x1: int or float, y1: int or float, x2: int or float, y2: int or float):
    if abs(x1) + abs(y1) < abs(x2) + abs(y2):
        return f"({floor(x1)}, {floor(y1)})"
    return f"({floor(x2)}, {floor(y2)})"


x1_coordinate = float(input())
y1_coordinate = float(input())
x2_coordinate = float(input())
y2_coordinate = float(input())
print(center_point(x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate))
