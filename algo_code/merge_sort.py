def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение массива на две части
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Слияние отсортированных частей
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Слияние двух массивов
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавление оставшихся элементов
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Пример
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print('Отсортированный массив:', sorted_arr)