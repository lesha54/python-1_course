import random

def linear_search(arr, search_val):
    count_of_comparisons = 0
    for i in range(len(arr)):
        count_of_comparisons += 1
        if arr[i] == search_val:
            return i, count_of_comparisons
    return -1, count_of_comparisons

def binary_search(arr, search_val):
    count_of_comparisons = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        count_of_comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == search_val:
            return mid, count_of_comparisons
        elif arr[mid] < search_val:
            low = mid + 1
        else:
            high = mid - 1
    return -1, count_of_comparisons

arr = sorted(random.sample(range(1000001), 100))
print("Сгенерированный список чисел:")
print(arr)
search_val = int(input(f"введите чиcло для поиска: "))

index_of_linear, count_of_linear = linear_search(arr, search_val)
index_of_binary, count_of_binary = binary_search(arr, search_val)

if index_of_linear != -1:
    print("элемент найден")
    print(f"бинарный поиск: индекс {index_of_binary}, сравнений {count_of_binary}")
    print(f"динейный поиск: индекс {index_of_linear}, сравнений {count_of_linear}")
else:
    print("элемент не найден ни в одном из поисков")


