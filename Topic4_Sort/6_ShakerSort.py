def shaker_sort(arr): # O(n^2)
    left = 0
    right = len(arr) - 1
    while left < right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr

arr = [2, 5, 7, 3, 1, 9, 10, 14, 20, 11, 0]
print(shaker_sort(arr))