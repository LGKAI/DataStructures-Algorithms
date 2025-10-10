def interchange_sort(arr): # O(n^2)
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]: arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [2, 5, 7, 3, 1, 9, 10, 14, 20, 11, 0]
print(interchange_sort(arr))