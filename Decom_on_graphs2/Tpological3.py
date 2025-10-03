graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
}

def topological_sort(graph):

    visited = {}
    order = []

    def dfs(node):

        if node not in visited:
            visited[node] = True
            for neighbord in graph[node]:
                dfs(neighbord)
            order.append(node)

    for node in graph:
        dfs(node)
    
    return order[::-1]
        
print("Topological Sort:", topological_sort(graph))