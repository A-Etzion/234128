def NxNmatrix(mat, n):
    if len(mat) > n :
        for row in mat :
            row = row[0:n]
        mat = mat[0:n]
    else :
        for row in mat :
            row.extend([0]*(n-len(mat)))
        for i in range(n-len(mat)):
            mat.append([0]*n)

def isCellSpecial(mat, i, j):
    smaller_than = 0
    equal = 0
    for k in range(len(mat)):
        if mat[i][j]==mat[k][j]:
            equal+=1
        if mat[i][j]>mat[k][j]:
            smaller_than+=1
    for p in range(len(mat)):
        if mat[i][j]==mat[i][p]:
            equal-=1
        if mat[i][j]>mat[i][p]:
            smaller_than-=1
    if (smaller_than+equal)==0:
        return True
    return False



length = int(input())
column = int(input())
matrix = []
tmp_list = []
for i in range(length):
    tmp_list.append(i)
    if (( i+1 ) % column ) == 0:
        matrix.append(tmp_list)
        tmp_list = []
if len(tmp_list)>0 :
    matrix.append(tmp_list)

for row in matrix :
    if len(row) < column :
        for j in range(column-len(row)):
            row.append(0)

print(matrix)
n = int(input())
NxNmatrix(matrix,n)
print(matrix)
i = int(input())
j = int(input())
special = isCellSpecial(matrix,i,j)
print(special)
