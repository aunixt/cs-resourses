matrixs = {}
row_and_col = []
for c in range(3):
    i, j = map(int, input().split())
    matrix = []
    for _ in range(i):
        input_row = input().split()
        a_row = [int(x) for x in input_row]
        matrix.append(a_row)
    matrixs[c] = matrix
    row_and_col.append((i, j))

i1, j1 = row_and_col[0]
i2, j2 = row_and_col[1]
i3, j3 = row_and_col[2]
flag = (j1 == i2 and i1 == i3 and j2 == j3)

if not flag:
    print('Error!')
else:
    new_matrix1 = []
    for a in range(i1):
        row = []
        for b in range(j2):
            num = sum(matrixs[0][a][r] * matrixs[1][r][b] for r in range(j1))
            row.append(num)
        new_matrix1.append(row)

    new_matrix2 = []
    for m in range(i3):
        row = []
        for n in range(j3):
            row.append(new_matrix1[m][n] + matrixs[2][m][n])
        new_matrix2.append(row)

    for k in range(i3):
        print(*new_matrix2[k])