def find_min_edge(visited):
    min_cost = 99999
    min_edge = ()
    for j in visited:
        for i in graph[j]:
            if i[1] < min_cost and i[0] not in visited: 
                min_cost = i[1]
                min_edge = i
                src = j
                dest = i[0]
                
    print(src,"->",min_edge)
    return min_edge

def Prims():
    visited = []
    cost = 0
    visited.append("A")
    while len(visited) != len(graph.keys()):
        min_edge = find_min_edge(visited)
        if len(min_edge):
            visited.append(min_edge[0])
            cost+=min_edge[1]
            
    print("Total Cost : " , cost)
            
          

graph = {"A" : [["B", 1],["D", 3]],
         "B" : [["A", 1],["E", 4],["C", 2]],
         "C" : [["B", 2],["D", 5]],
         "D" : [["A", 3],["C", 5]],
         "E" : [["B", 4]]}

graph = {
    "A": [["B", 2], ["C", 3]],
    "B": [["A", 2], ["D", 1]],
    "C": [["A", 3], ["D", 4]],
    "D": [["B", 1], ["C", 4]]
}


# Choosing 'A' as Start Node.
Prims()