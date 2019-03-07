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
graph = {}
index = 0
for vertex in matrix:
    adjacenVertices = []
    adjacentVertex = 0
    degree = 0
    for edge in vertex:
        if edge == 1:
            degree += 1
            adjacenVertices.append(adjacentVertex)
        adjacentVertex += 1
    v = {index: set(adjacenVertices)}
    graph.update(v)
    index += 1;

def dfs(graph, start):
    path = []
    component = []
    vertices = []
    for v in graph:
        vertices.append(v)
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component.append(vertex)
            visited.add(vertex)
            vertices.remove(vertex)
            stack.extend(graph[vertex] - visited)
        if not stack and vertices:
            path.append(component)
            component = []
            stack.append(vertices[0])
        if not stack and not vertices:
            path.append(component)
    return path

graphComponents = dfs(graph, 0)

nextVertices = []
for component in graphComponents:
    for vertex in component:
        nextVertices.append(vertex)
print("Wierzchołki w kolejności ich rozpatrzenia:")
print(nextVertices)
print("Liczba składowych spójności: " + str(len(graphComponents)))
print("Kolejne składowe spójności:")
for component in graphComponents:
    print(component)