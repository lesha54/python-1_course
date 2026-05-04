import math

def calculate_pyramid_volume():
    print("объем усеченной пирамиды ")
    try:
        square1 = float(input("введите площадь нижнего основания "))
        square2 = float(input("введите площадь верхнего основания "))
        high = float(input("введите высоту пирамиды "))
        volume = (1/3) * high * (square1 + square2 + math.sqrt(square1 * square2))
        print(f"объем пирамиды равен {volume} ")
        return volume
    except ValueError:
        print("ошибка: нужно вводить числа ")
