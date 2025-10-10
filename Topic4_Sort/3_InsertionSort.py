def insertion_sort(arr): # O(n^2)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [2, 5, 7, 3, 1, 9, 10, 14, 20, 11, 0]
print(insertion_sort(arr))