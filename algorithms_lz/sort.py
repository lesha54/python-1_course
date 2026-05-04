import os
import random

if os.name == 'nt':
    os.system('chcp 65001 > nul')

def bubble_sort(numbers):
    count = len(numbers)
    arr = list(numbers)
    count_of_comparisons = 0
    for i in range(count):
        for j in range(0, count - i - 1):
            count_of_comparisons += 1 
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
        print(f"сортировка пузырьком, итерация {i+1}: {arr}")
    return arr, count_of_comparisons

def selection_sort(numbers):
    count = len(numbers)
    arr = list(numbers)
    count_of_comparisons = 0
    for i in range(count):
        max_value = i
        for j in range(i + 1, count):
            count_of_comparisons += 1
            if arr[j] > arr[max_value]:
                max_value = j
        arr[i], arr[max_value] = arr[max_value], arr[i]
        print(f"сортировка выбором, итерация {i+1}: {arr}")
        return arr, count_of_comparisons
    

numbers = [random.randint(0, 1000000) for _ in range(100)]
print("сортировка пузырьком")
sorted_bubble, comparisons_bubble = bubble_sort(numbers)
print("сортировка выбором")
sorted_selection, comparisons_selection = selection_sort(numbers)

print("результат")
print(f"отсортированный список: {sorted_bubble}")
print(f"сравнений в 1 сортировке: {comparisons_bubble}")
print(f"сравнений во 2 сортировке: {comparisons_selection}")