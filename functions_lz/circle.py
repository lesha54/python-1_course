import math
radius = float(input())

def area(radius):
    area = math.pi * (radius ** 2)
    return area

def lengthOfCircle(radius):
    length = 2 * math.pi * radius
    return length

print(area(radius))
print(lengthOfCircle(radius))