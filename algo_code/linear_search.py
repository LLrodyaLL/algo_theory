def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Пример
arr = [5, 3, 6, 1, 9]
target_1 = 7
target_2 = 3
result_1 = linear_search(arr, target_1)
result_2 = linear_search(arr, target_2)
print(f'Элемент для первого примера найден на индексе: {result_1}' if result_1 != -1 else 'Элемент не найден для первого примера')
print()
print(f'Элемент для второго примера найден на индексе: {result_2}' if result_2 != -1 else 'Элемент не найден для второго примера')