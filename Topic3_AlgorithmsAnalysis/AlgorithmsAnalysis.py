def find_k_smallest(arr, k):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[k - 1]
# Độ phức tạp: O(n^2)

def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices cannot be added")
    result = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    return result
# Độ phức tạp: O(n^2)

def multiply_matrices(a, b):
    if not a or not b:
        raise ValueError("One or both matrices are empty")
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise ValueError("Matrices cannot be multiplied")
    res = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                res[i][j] += a[i][k] * b[k][j]
    return res
# Độ phức tạp: O(n^3)

def transpose_matrix(matrix: list) -> list:
    if not matrix:
        return []
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
# Độ phức tạp: O(n^2)

if __name__ == '__main__':
    arr = [3, 5, 2, 1, 7]
    print(find_k_smallest(arr, 2))