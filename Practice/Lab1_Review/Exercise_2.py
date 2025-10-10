def read_matrix(filename: str) -> list:
    with open(filename, 'r') as file:
        lines = file.readlines()
    matrix = []
    for line in lines[1:]:
        row = list(map(int, line.split()))
        matrix.append(row)
    return matrix

def print_matrix(filename: str, matrix: list) -> None:
    with open(filename, 'w') as file:
        rows = len(matrix)
        cols = len(matrix[0]) if matrix else 0
        file.write(f"{rows} {cols}\n")
        for row in matrix:
            file.write(" ".join(map(str, row)) + "\n")

def multiply_matrices(a: list, b: list) -> list:
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

def transpose_matrix(matrix: list) -> list:
    if not matrix:
        return []
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


if __name__ == '__main__':
    a = read_matrix("matrix_a.txt")
    b = read_matrix("matrix_b.txt")

    try:
        c = multiply_matrices(a, b)
        print_matrix("matrix_c.txt", c)
        
        c_transposed = transpose_matrix(c)
        print_matrix("matrix_c_transposed.txt", c_transposed)
    
    except ValueError as e:
        print(e)
    
