def linear_search(arr, target): # O(n)
    for i in range(len(arr)):
        if arr[i] == target: return i
    return -1

def linear_search_with_sentinel(arr, target): # phiên bản có lính canh
    n = len(arr)
    arr.append(target) # thêm lính canh vào cuối mảng
    i = 0
    while arr[i] != target:
        i += 1
    arr.pop() # xoá lính canh để khôi phục mảng ban đầu
    if i < n:
        return i # tìm thấy phần tử ở vị trí i
    else:
        return -1 # không tìm thấy

arr = [1, 5, 7, 3, 4, 3]
print(linear_search(arr, 3))
print(linear_search_with_sentinel(arr, 3))