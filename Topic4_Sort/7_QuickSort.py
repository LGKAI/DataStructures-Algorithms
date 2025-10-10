def quick_sort(arr, left, right): # O(nlogn)
    if left >= right: return
    i, j = left, right
    pivot = arr[(left + right) // 2]
    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if left < j: quick_sort(arr, left, j)
    if i < right: quick_sort(arr, i, right)

def quick_sort_iterative(arr): # phiên bản ko đệ quy
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        # Chọn pivot là phần tử giữa
        mid = (start + end) // 2
        pivot = arr[mid]
        # Partition (kiểu Lomuto được chỉnh sửa để xử lý pivot giữa)
        i, j = start, end
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        # Đẩy 2 phần con chưa sắp xếp vào stack
        if start < j:
            stack.append((start, j))
        if i < end:
            stack.append((i, end))
    return arr

arr = [2, 5, 7, 3, 1, 9, 10, 14, 20, 11, 0]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
print(quick_sort_iterative(arr))