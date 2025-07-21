class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y




pt1 = Point()
pt1.set_coords(1, 2)


pt2 = Point()
pt2.set_coords(10, 20)
print(f"pt1 x = {pt1.x}, pt2 x = {pt2.x}")
print(f"pt1 y = {pt1.y}, pt2 y = {pt2.y}")
