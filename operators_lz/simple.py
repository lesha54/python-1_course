import math
print('Введите число для проверки на простоту')
number = int(input())

def Issimple(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True
    
a = print(Issimple(number))