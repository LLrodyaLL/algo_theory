def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для отслеживания изменений на текущем проходе
        swapped = False
        # Проход по массиву до n-i-1, так как последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если не было обменов, массив уже отсортирован
        if not swapped:
            break

# Пример
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Отсортированный массив:", arr)