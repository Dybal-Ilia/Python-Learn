class Point:
    color = 'red'
    circle = 2



point1 = Point()
point2 = Point()

print(f"point1 color = {point1.color}")
print(f"point2 circle = {point2.circle}")


point1.color = 'blue'
print(f"point1 color = {point1.color}")
point1.color = Point.color
print(f"point1 color = {point1.color}")

point1.x = 1
point1.y = -3

point2.x = 0
point2.y = 10