from random import randint
import timeit
def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key
    return arr
def selection_sort(arr):
    for i in range(len(arr) - 1):
        mn_in = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mn_in]:
                mn_in = j
        arr[i], arr[mn_in] = arr[mn_in], arr[i]
    return arr
def compare(arr_len):
    arr = [randint(1, 100) for _ in range(arr_len)]
    a = timeit.timeit(lambda: bubble_sort(arr), number=1000)
    b = timeit.timeit(lambda: insertion_sort(arr), number=1000)
    c = timeit.timeit(lambda: selection_sort(arr), number=1000)
    print(f'время сортировки пузырьком: {a*1000:.5}; вставками: {b*1000:.5}; выбором: {c*1000:.5}')

compare(10)
compare(100)
compare(1000)
