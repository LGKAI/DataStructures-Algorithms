def binary_search(arr, left, right, key):
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < key: left = mid + 1
        else: right = mid
    return left

def binary_insertion_sort(arr): # O(n^2)
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, 0, i, key)
        j = i
        while j > pos:
            arr[j] = arr[j - 1]
            j -= 1
        arr[pos] = key
    return arr

arr = [2, 5, 7, 3, 1, 9, 10, 14, 20, 11, 0]
print(binary_insertion_sort(arr))