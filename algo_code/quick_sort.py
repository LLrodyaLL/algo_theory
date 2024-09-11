def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] # выбор опорного элемента (средний элемент)
        left = [x for x in arr if x < pivot] # элементы меньше опорного
        middle = [x for x in arr if x == pivot] # элементы равные опорному
        right = [x for x in arr if x > pivot] # элементы больше опорного
        return quick_sort(left) + middle + quick_sort(right)

# Пример
arr = [3, 6, 8, 10, 1, 2, 1]
print('Отсортированный массив:', quick_sort(arr))