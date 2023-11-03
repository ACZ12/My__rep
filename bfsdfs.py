import collections


graph={
    
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[],
}
visited=[]
def dfs(visited,graph,root):
    if root not in visited:
        visited.append(root)
        for neighbor in graph[root]:
            dfs(visited,graph,neighbor)
dfs(visited,graph,"A")
#print(visited)

visited=[]
def dfs(visited,graph,root):
    if root not in visited:
        visited.append(root)
        for n in graph[root]:
            dfs(visited,graph,n)
dfs(visited,graph,"A")
print(visited)


graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[],
}
def bfs(graph,root):
    visited=[]
    queue=collections.deque([root])
    while queue:
        vertex=queue.popleft()
        visited.append(vertex)
        for n in graph[vertex]:
            if n not in visited:
                queue.append(n)
bfs(graph,"A")
#print(visited)