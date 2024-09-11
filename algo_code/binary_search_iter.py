def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Пример
arr = [1, 3, 5, 7, 9, 11]
target_1 = 7
target_2 = 4
result_1 = binary_search(arr, target_1)
result_2 = binary_search(arr, target_2)
print(f'Элемент для первого пример найден на индексе {result_1}' if result_1 != -1 else 'Элемент не найден для первого примера')
print()
print(f'Элемент для второго пример найден на индексе {result_2}' if result_2 != -1 else 'Элемент не найден для второго примера')
