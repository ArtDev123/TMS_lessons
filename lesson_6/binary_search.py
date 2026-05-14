# def binary_search(arr: list[int], target: int) -> int:
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]

#         if guess == target:
#             return mid  # Элемент найден, возвращаем индекс
#         if guess > target:
#             high = mid - 1  # Ищем в левой половине
#         else:
#             low = mid + 1  # Ищем в правой половине

#     return -1  # Элемент не найден


# some_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = binary_search(some_list, 3)
# print(res)

counter = 0


def binary_search_recursive(arr: list[int], target: int, low: int, high: int) -> int:
    # Базовый случай: диапазон поиска пуст
    if low > high:
        return -1

    mid = (low + high) // 2
    guess = arr[mid]

    if guess == target:
        return mid
    elif guess > target:
        # Рекурсивный поиск в левой части
        return binary_search_recursive(arr, target, low=low, high=mid - 1)
    else:
        # Рекурсивный поиск в правой части
        return binary_search_recursive(arr, target, low=mid + 1, high=high)


my_list: list[str] = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 22, 23, 25]

target_value: int = 7

result_rec = binary_search_recursive(my_list, target_value, 0, len(my_list) - 1)

print(result_rec)
print(counter)
