def generate_permutations(arr, start):
    if start == len(arr):
        print(*arr) # in mảng các phần tử cách nhau bằng khoảng trắng
    else:
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start] # hoán đổi
            generate_permutations(arr, start + 1) # đệ quy phần còn lại
            arr[start], arr[i] = arr[i], arr[start] # đổi lại

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    generate_permutations(nums, 0)