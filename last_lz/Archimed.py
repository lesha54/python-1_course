def check_buoyancy():
    print("закон Архимеда ")
    try:
        massa = float(input("введите массу тела в кг "))
        volume_part = float(input("введите объем погруженной части в м3 "))
        density_obj = float(input("введите плотность объекта в кг/м3 "))
        density_water = 1 
        can_swimming = lambda massa, volume_part, dwnsity_water: (density_water * volume_part) >= massa
        if can_swimming(massa, volume_part, density_water):
            print("объект плавает ")
        else:
            print("объект тонет ")
    except ValueError:
        print("ошибка: вводите только числа ")
