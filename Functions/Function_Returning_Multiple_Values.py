import math
def calculateProperty(radius):
    area = math.pi * (radius ** 2)
    circum = 2 * math.pi * radius
    return area, circum

area, circum = calculateProperty(10)
print("Area of the circle is", round(area,3))
print("Circumference of the circle is", round(circum,3))