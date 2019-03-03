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

# displaying edges
edges = []
index = 0
for vertex in matrix:
    index1 = 0
    for edge in vertex:
        edgeArr = []
        if edge == 1:
            edgeArr.append(index)
            edgeArr.append(index1)
        if edgeArr:
            edges.append(edgeArr)
        index1 += 1
    edgeArr = []
    index += 1

seen = set()
unique = []
for edge in edges:
    srtd = tuple(sorted(edge))
    if srtd not in seen:
            unique.append(edge)
            seen.add(srtd)
edges = unique
print('Edges:')
print(edges)

incidence_matrix = []
index = 0
for vertex in matrix:
    inner_matrix = []
    for edge in edges:
        if edge[0] == index or edge[1] == index:
            inner_matrix.append(1)
        else:
            inner_matrix.append(0)
    incidence_matrix.append(inner_matrix)
    index += 1
print('Incidence matrix:')
for x in incidence_matrix:
    print(x)