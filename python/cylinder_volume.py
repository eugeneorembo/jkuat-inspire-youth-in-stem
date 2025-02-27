import math
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

radius = int(input("enter the radius of the cylinder: "))
height = int(input("enter the height of the cylinder: "))
print(cylinder_volume(radius, height))

