def convert_to_base(number, base):
    digits = "0123456789ABCDEF"
    if number < base:
        return digits[number]
    else:
        return convert_to_base(number // base, base) + digits[number % base]

print("перевод числа в систему счисления")
number = int(input("введите число: "))
base = int(input("введите основание: "))
result = convert_to_base(number, base)
print(f"Результат: {result}")
