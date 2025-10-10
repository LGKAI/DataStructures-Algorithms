def bubble_sort(arr, reverse = False):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if (not reverse and arr[j] > arr[j + 1]) or (reverse and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort_even_odd(arr):
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    evens = bubble_sort(evens)
    odds = bubble_sort(odds, reverse = True)
    res = []
    for x in arr:
        if x % 2 == 0: res.append(evens.pop(0))
        else: res.append(odds.pop(0))
    return ' '.join(map(str, res))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(sort_even_odd(arr))