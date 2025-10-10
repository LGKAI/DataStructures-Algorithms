import sys

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def linear_search_sentinel(arr, x):
    n = len(arr)
    last = arr[-1]
    arr[-1] = x  # đặt lính canh
    i = 0
    while arr[i] != x:
        i += 1
    arr[-1] = last  # khôi phục phần tử cuối cùng
    if i < n - 1 or arr[-1] == x:
        return i
    return -1

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            while mid > 0 and arr[mid - 1] == x:
                mid -= 1  # tìm vị trí đầu tiên
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def interpolation_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] <= x <= arr[right]:
        if left == right:
            if arr[left] == x:
                return left
            return -1
        pos = left + ((right - left) // (arr[right] - arr[left]) * (x - arr[left]))
        if pos < left or pos > right:
            return -1
        if arr[pos] == x:
            while pos > 0 and arr[pos - 1] == x:
                pos -= 1  # tìm vị trí đầu tiên
            return pos
        if arr[pos] < x:
            left = pos + 1
        else:
            right = pos - 1
    return -1

def main():
    if len(sys.argv) != 5:
        print("Usage: python Exercise_1.py algorithm x input_path output_path")
        return
    
    algorithm = int(sys.argv[1])
    x = int(sys.argv[2])
    input_path = sys.argv[3]
    output_path = sys.argv[4]
    
    with open(input_path, 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))
    
    if algorithm == 1:
        result = linear_search(arr, x)
    elif algorithm == 2:
        result = linear_search_sentinel(arr, x)
    elif algorithm == 3:
        result = binary_search(arr, x)
    elif algorithm == 4:
        result = interpolation_search(arr, x)
    else:
        print("Invalid algorithm choice")
        return
    
    with open(output_path, 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()