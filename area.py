import math
def rectangle(width, height):
    area = width * height
    return area


print(rectangle(3, 5))
print(rectangle(7,4))


def triangle(base,height):
    area = base*height*0.5
    return area

print(triangle(4,3))


def circle(radius):
    area = math.pi * radius * radius
    return round(area,4)

print(circle(3))