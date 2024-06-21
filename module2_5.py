def get_matrix(n, m, value):
    matrix = []
    for stroka in range(n):
        matrix.append(list())
        for stolb in list(range(m)):
            matrix[-1].append(value)
    return matrix
matrix = get_matrix(4, 5, 28)
matrix2 = get_matrix(2, 3, 7)
matrix3 = get_matrix(5, 2, 15)
print(matrix)
print(matrix2)
print(matrix3)