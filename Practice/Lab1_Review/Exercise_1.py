def input_list(n: int) -> list:
    lst = []
    for i in range(n):
        element = int(input(f"Please input element {i + 1}: "))
        lst.append(element)
    return lst

def print_list(arr: list) -> None:
    print(", ".join(map(str, arr)))

def find_max(arr: list) -> int:
    max_value = arr[0]
    for i in arr[1:]:
        if i > max_value:
            max_value = i
    return max_value

def sum_list(arr: list) -> int:
    total = 0
    for i in arr:
        total += i
    return total

def concat_lists(a: list, b: list) -> list:
    return a + b

def find_longest_ascending_sublist(arr: list) -> list:
    if not arr:
        return []
    
    longest = []
    cur = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            cur.append(arr[i])
        else:
            if len(cur) > len(longest):
                longest = cur
            cur = [arr[i]]

    if len(cur) > len(longest):
        longest = cur

    return longest


if __name__ == '__main__':
    length_a = int(input("Enter the number of elements in list a: "))
    a = input_list(length_a)

    length_b = int(input("Enter the number of elements in list b: "))
    b = input_list(length_b)

    c = concat_lists(a, b)
    print("The concatenated list c:", end=" ")
    print_list(c)

    print("The maximum value in list c:", end=" ")
    print(find_max(c))

    print("The sum of elements in list c:", end=" ")
    print(sum_list(c))

    print("The longest ascending sublist in list c:", end=" ")
    print(find_longest_ascending_sublist(c))