def merge(left, right):
    sorted_lst = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1
    sorted_lst.extend(left[i:])
    sorted_lst.extend(right[j:])
    return sorted_lst

def merge_sort(arr): # O(nlogn)
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge_sort_iterative(arr): # phiên bản ko đệ quy
    width = 1
    n = len(arr)
    # Tạo mảng tạm để lưu kết quả hợp nhất
    result = arr[:]
    while width < n:
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)
            # Hợp nhất hai nửa đã sắp xếp
            l, r = left, mid
            temp = []
            while l < mid and r < right:
                if result[l] <= result[r]:
                    temp.append(result[l])
                    l += 1
                else:
                    temp.append(result[r])
                    r += 1
            temp.extend(result[l:mid])
            temp.extend(result[r:right])
            result[left:right] = temp
        width *= 2
    return result

arr = [2, 5, 7, 3, 1, 9, 10, 14, 20, 11, 0]
print(merge_sort(arr))
print(merge_sort_iterative(arr))