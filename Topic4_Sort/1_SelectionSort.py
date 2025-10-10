def selection_sort(arr): # O(n^2)
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]: min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    
arr = [2, 5, 7, 3, 1, 9, 10, 14, 20, 11, 0]
print(selection_sort(arr))