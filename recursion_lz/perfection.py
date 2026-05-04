def sum_divisors(number,divisor = 1):
    if divisor == number:
        return 0
    
    if number % divisor == 0:
        return divisor + sum_divisors(number, divisor + 1)
    else:
        return sum_divisors(number, divisor + 1)

def is_perfect_number(n):
    return sum_divisors(n) == n

print("проверка на совершенное число")
number = int(input("введите число для проверки: "))

if is_perfect_number(number):
    print(f"число {number} является совершенным")
else:
    print(f"число {number} не совершенное.")

