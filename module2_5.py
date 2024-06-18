def get_matrix():
    n = 4
    m = 5
    value = 28
    matrix = []
    for stroka in range(n):
        matrix.append(list())
        for stolb in list(range(m)):
            matrix[-1].append(value)
    return matrix
matrix = get_matrix()
print(matrix)