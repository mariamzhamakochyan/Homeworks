rows = int(input("Give the number of rows: "))  
columns = int(input("Give the number of columns: "))  
matrix = []  
for i in range(rows): 
    r = []  
    for j in range(columns):   
        r.append(int(input("Enter the rows and columns: ")))  
    matrix.append(r)  
 
for i in range(rows):  
    for j in range(columns):  
        print(matrix[i][j], end=" ")  
    print()  
