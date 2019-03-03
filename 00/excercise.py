# Get matrix from graph.txt and convert it into 2d array
matrix = []
f=open("graph.txt", "r")
if f.mode == "r":
    f1 = f.readlines()
    for vertex in f1:
        inner_matrix = []
        for char in vertex:
            if char=='0' or char=='1':
                num = int(char)
                inner_matrix.append(num)
        matrix.append(inner_matrix)
