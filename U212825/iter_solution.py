def levenshtein(i, j):
    matrix = [[0] * j for _ in range(i)]
    matrix[0][:] = range(j)
    for k in range(i):
        matrix[k][0] = k

    for ii in range(1, i):
        for jj in range(1, j):
            matrix[ii][jj] = min(
                matrix[ii - 1][jj],
                matrix[ii][jj - 1],
                matrix[ii - 1][jj - 1] - (s1[ii - 1] == s2[jj - 1])
            ) + 1

    return matrix[-1][-1]


if __name__ == '__main__':
    s1, s2 = input().split()
    print(levenshtein(len(s1) + 1, len(s2) + 1))
