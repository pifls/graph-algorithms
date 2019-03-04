# Get matrix from matrixDFS.txt and convert it into 2d array
matrix = []
f=open("matrixDFS.txt", "r")
if f.mode == "r":
    f1 = f.readlines()
    for vertex in f1:
        inner_matrix = []
        for char in vertex:
            if char=='0' or char=='1':
                edge = int(char)
                inner_matrix.append(edge)
        matrix.append(inner_matrix)
