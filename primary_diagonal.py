def read_matrix(is_test=False):
    if is_test :
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(rows_count):
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)

        return matrix

def get_primary_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

def get_sum_below_primary_diagonal_1(matrix):
    the_sum = 0
    size =len(matrix)
    for r in range(size):
        for c in range(size):
            if r < c:
        # for c in range(r):# excl with diagonal
                the_sum += matrix[r][c]
    return the_sum

def get_sum_below_primary_diagonal_2(matrix):
    the_sum = 0
    size =len(matrix)
    for r in range(size):
        for c in range(size):
            if r < c:
                break
            # for c in range(r):# excl with diagonal
        the_sum += matrix[r][c]
    return the_sum

def get_sum_below_primary_diagonal_3(matrix):
    the_sum = 0
    size =len(matrix)
    for r in range(size):
        for c in range(r + 1):# incl with diagonal
            # for c in range(r):# excl with diagonal
            the_sum += matrix[r][c]
    return the_sum

print(get_primary_diagonal_sum(read_matrix(is_test=True)))
print(get_sum_below_primary_diagonal_1(read_matrix(is_test=True)))
print(get_sum_below_primary_diagonal_2(read_matrix(is_test=True)))
print(get_sum_below_primary_diagonal_3(read_matrix(is_test=True)))
