def get_digit(num, digit_index):
    return (num // (10 ** digit_index)) % 10

def radix_sort(arr): # O(nk)
    max_val = max(arr)
    max_digits = len(str(max_val))
    for digit_index in range(max_digits):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = get_digit(num, digit_index)
            buckets[digit].append(num)
        arr.clear()
        for bucket in buckets:
            arr.extend(bucket)

arr = [2, 5, 7, 3, 1, 9, 10, 14, 20, 11, 0]
radix_sort(arr)
print(arr)