def insertionSort(arr):
    for i in range(len(arr) - 1):
        j = i
        while arr[j] > arr[j + 1] and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr
