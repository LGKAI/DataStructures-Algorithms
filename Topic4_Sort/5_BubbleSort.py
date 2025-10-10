def bubble_sort(arr): # O(n^2)
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break

arr = [2, 5, 7, 3, 1, 9, 10, 14, 20, 11, 0]
bubble_sort(arr)
print(arr)