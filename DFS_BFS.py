def dfs(node,visit):
    print(node, end = ' ')
    visit.append(node)
    for i in graph[node]:
        if i not in visit:
            dfs(i,visit)
    
    

graph = {"A" : ["B","C"],
         "B" : ["A" , "D"],
         "C" : ["A", "D"],
         "D" : ["B" , "C"]}



print("Depth First Search : " , end = ' ')
dfs("D",[])

print("\nBreadth First Search : " , end = ' ')
que = []
visited = []
que.append("D")

while que:
    temp = que.pop(0)
    print(temp , end = ' ')
    visited.append(temp)
    for i in graph[temp]:
        if i not in visited and i not in que:
            que.append(i)
            
            

