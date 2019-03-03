# Get matrix from graph.txt and convert it into 2d array
matrix = []
f=open("graph.txt", "r")
if f.mode == "r":
    f1 = f.readlines()
    for vertex in f1:
        inner_matrix = []
        for char in vertex:
            if char=='0' or char=='1':
                edge = int(char)
                inner_matrix.append(edge)
        matrix.append(inner_matrix)

# displaying degree of vertices 
index = 0
mostEdges = 0
for vertex in matrix:
    degree = 0
    for edge in vertex:
        if edge == 1:
            degree += 1
        if mostEdges < degree:
            mostEdges = degree
    print('Degree of vertex ' + str(index) + ': ' + str(degree))
    index += 1;

# displaying adjacent vertices of vertex or vertices with highest degree
index = 0
for vertex in matrix:
    adjacenVertives = []
    adjacentVertex = 0
    degree = 0
    for edge in vertex:
        if edge == 1:
            degree += 1
            adjacenVertives.append(adjacentVertex)
        adjacentVertex += 1
    if degree == mostEdges:
        print('Adjacent vertices of vertex ' + str(index) + ': ' + str(adjacenVertives))
    index += 1;