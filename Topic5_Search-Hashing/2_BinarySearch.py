def binary_search(arr, target): # O(logn)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    if left > right: return -1
    mid = (left + right) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: return binary_search_recursive(arr, target, mid + 1, right)
    else: return binary_search_recursive(arr, left, mid - 1)

arr = [1, 1, 2, 3, 4, 5, 6]
print(binary_search(arr, 1))
print(binary_search_recursive(arr, 3, 0, len(arr) - 1))