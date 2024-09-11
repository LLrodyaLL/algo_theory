def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Сдвигаем элементы arr[0..i-1], которые больше key, на одну позицию вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Пример
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print('Отсортированный массив:', arr)