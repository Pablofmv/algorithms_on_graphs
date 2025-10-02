graph = {
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['F', 'G'],
    'E': ['G'],
    'F': [],
    'G': []
}

def topological_sort(graph):

    visited = {}
    order = []

    def dfs(node):
        if node not in visited:
            visited[node] = True
            for neighbor in graph[node]:
                dfs(neighbor)
            order.append(node)
    
    for node in graph:
        dfs(node)
    
    return order[::-1]

print("Topological Sort:", topological_sort(graph))
    


        