import timeit
import random

# Функція для генерації тестових даних
def generate_data(size):
    return [random.randint(0, size) for _ in range(size)]

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Стандартна реалізація Timsort в Python
def tim_sort(arr):
    arr.sort()

# Функція для тестування швидкості сортування
def test_sorting_algorithm(algorithm, size):
    setup_code = f"from __main__ import {algorithm}, generate_data"
    stmt = f"data = generate_data({size}); {algorithm}(data)"
    time = timeit.timeit(stmt, setup=setup_code, number=1)
    return time

if __name__ == "__main__":
    # Задайте розмір тестових даних
    data_sizes = [1000, 10000, 100000]  # Розмір списку для тестування

    # Проведення тестування для кожного алгоритму та розміру даних
    algorithms = ["merge_sort", "insertion_sort", "tim_sort"]

    for size in data_sizes:
        print(f"Розмір даних: {size}")
        for algorithm in algorithms:
            time = test_sorting_algorithm(algorithm, size)
            print(f"Алгоритм: {algorithm}, Час виконання: {time}")
        print()
