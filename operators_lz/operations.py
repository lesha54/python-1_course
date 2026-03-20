print('Введите одно число')
number = int(input())
count = 0
def countOfOperat(number, count):
    while(number > 0):
        number -= 3
        count += 1
    return count

a= print(int(countOfOperat(number, count)))