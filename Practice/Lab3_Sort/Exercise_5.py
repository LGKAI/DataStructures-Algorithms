import time
import random
import matplotlib.pyplot as plt


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr
# Độ phức tạp: O(n^2)


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
# Độ phức tạp: O(n^2)


def interchange_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
# Độ phức tạp: O(n^2)


def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def sort(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        return arr

    return sort(arr)
# Độ phức tạp: O(nlogn)


def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            sort(arr, low, pivot_index - 1)
            sort(arr, pivot_index + 1, high)

    sort(arr, 0, len(arr) - 1)
    return arr
# Độ phức tạp: O(n^2)


def merge_sort(arr):
    def merge(arr, left, mid, right):
        n1, n2 = mid - left + 1, right - mid
        L, R = arr[left:mid + 1], arr[mid + 1:right + 1]
        i, j, k = 0, 0, left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            k += 1
            i += 1
        while j < n2:
            arr[k] = R[j]
            k += 1
            j += 1

    def sort(arr, left, right):
        if left < right:
            mid = (right + left) // 2
            sort(arr, left, mid)
            sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

    sort(arr, 0, len(arr) - 1)
    return arr
# Độ phức tạp: O(n)


def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)

    return sorted_arr
# Độ phức tạp: O(n+k) với n là len(arr) và k là max(arr)


def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)
        arr = [num for bucket in buckets for num in bucket]
        exp *= 10

    return arr
# Độ phức tạp: O(n*k) với n là len(arr) và k là max(arr)


def flash_sort(arr):
    n = len(arr)
    if n == 0:
        return arr

    min_val, max_val = min(arr), max(arr)
    if min_val == max_val:
        return arr

    m = int(0.45 * n)
    count = [0] * m

    for num in arr:
        index = (m - 1) * (num - min_val) // (max_val - min_val)
        count[index] += 1

    for i in range(1, m):
        count[i] += count[i - 1]

    sorted_arr = [0] * n
    for num in reversed(arr):
        index = (m - 1) * (num - min_val) // (max_val - min_val)
        count[index] -= 1
        sorted_arr[count[index]] = num

    return sorted_arr
# Độ phức tạp: O(n)


def measure_sorting_times(func_sort, type_lst):
    def measure_time(sort_function, arr):
        arr_copy = arr[:]
        start_time = time.time()
        sort_function(arr_copy)
        return time.time() - start_time

    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
    times = []

    def random_array():
        for size in sizes:
            arr = [random.randint(1, 10000) for _ in range(size)]
            times.append(measure_time(func_sort, arr))

    def ascending_array():
        for size in sizes:
            arr = list(range(1, size + 1))
            times.append(measure_time(func_sort, arr))

    def descending_array():
        for size in sizes:
            arr = list(range(size, 0, -1))
            times.append(measure_time(func_sort, arr))

    array_types = {
        "ngau_nhien": random_array,
        "tang_dan": ascending_array,
        "giam_dan": descending_array,
    }

    array_types[type_lst]()

    plt.plot(sizes, times, marker="o", label=func_sort.__name__)
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Performance of {func_sort.__name__} on {type_lst} data")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # measure_sorting_times(insertion_sort, "tang_dan")
    # measure_sorting_times(selection_sort, "tang_dan")
    # measure_sorting_times(interchange_sort, "tang_dan")
    # measure_sorting_times(heap_sort, "tang_dan")
    # measure_sorting_times(quick_sort, "tang_dan")
    # measure_sorting_times(merge_sort, "tang_dan")
    # measure_sorting_times(counting_sort, "tang_dan")
    # measure_sorting_times(radix_sort, "tang_dan")
    measure_sorting_times(flash_sort, "tang_dan")