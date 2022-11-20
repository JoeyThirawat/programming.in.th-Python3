m, n = input().split()
m = int(m)
n = int(n)

matrix_a = []
matrix_b = []
matrix_c = []

for i in range(1, n):
    for j in range(1, m):
        matrix_a[i][j] = input().split()

for i in range(1, n):
    for j in range(1, m):
        matrix_b[i][j] = int(input())

for i in range(1, m):
    for j in range(1, n):
        matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]
        print(matrix_c[i][j])