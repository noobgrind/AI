def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootY] = rootX
        return True
    return False


graph = {"A" : [["B", 1],["D", 3]],
         "B" : [["A", 1],["E", 4],["C", 2]],
         "C" : [["B", 2],["D", 5]],
         "D" : [["A", 3],["C", 5]],
         "E" : [["B", 4]]}
graph = {
    "A": [["B", 5], ["D", 4]],
    "B": [["A", 5], ["C", 3], ["D", 2]],
    "C": [["B", 3], ["D", 6]],
    "D": [["B", 2], ["C", 6]]}
graph = {
    "A": [["B", 1], ["D", 4]],
    "B": [["A", 1], ["E", 2], ["C", 3]],
    "C": [["B", 3], ["F", 5]],
    "D": [["A", 4], ["E", 6]],
    "E": [["B", 2], ["D", 6], ["F", 7]],
    "F": [["C", 5], ["E", 7]]
}

parent = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F'
}


edges = []
for u in graph:
    for v, weight in graph[u]:
        if u < v:  
            edges.append([u, v, weight])
            
edges.sort(key = lambda x : x[2])
print(edges)

mst = []
cost = 0

for u, v, weight in edges:
    if union(u,v):
        mst.append([u,v,weight])
        cost += weight
        
print(mst)
print(cost)