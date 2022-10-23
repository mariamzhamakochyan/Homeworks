n = int(input("syunrti tivy: "))
m = int(input("toxeri tivy: "))
matrix = [[input("Enter a number: ") for i in range(n)] for j in range(m)]
print(matrix)
for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        print(matrix[i][j], end = ' ')
    print(' ')
