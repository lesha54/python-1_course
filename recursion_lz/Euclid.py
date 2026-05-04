def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(" НОД по алгоритму Евклида")
num1 = int(input("Введите первое число: "))
num2= int(input("Введите второе число: "))

result = gcd(num1, num2)
print(f"наибольший общий делитель: {result}")
