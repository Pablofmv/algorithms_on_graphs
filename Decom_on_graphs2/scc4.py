def strongly_connected_components(graph):

    #S1 - Build the reverse graph:

    reverse_graph = {}

    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in reverse_graph:
                reverse_graph[neighbor] = []
            reverse_graph[neighbor].append(node)
        
        if node not in reverse_graph:
            reverse_graph[node] = []
    
    #S2 - Run DFS on reverse_graph to get postorder number:

    visited_reverse = {}
    postorder = {}
    time = 1

    def dfs_reverse(node):
        nonlocal time
        visited_reverse[node] = True

        for neighbor in reverse_graph[node]:
            if neighbor not in visited_reverse:
                dfs_reverse(neighbor)
        
        postorder[node] = time
        time += 1
    
    for node in reverse_graph:
        if node not in visited_reverse:
            dfs_reverse(node)
    
    #S3 - Run DFS on graph following reverse post-order:

    visited = {}
    sccs = []

    def dfs_original(node,component):
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_original(neighbor, component)
    
    for v in sorted(postorder, key = postorder.get, reverse = True):
        if v not in visited:
            component = []
            dfs_original(v, component)
            sccs.append(component)
    
    return sccs

graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],   # Cycle 1: A-B-C
    'D': ['E'],
    'E': ['F'],
    'F': ['D']    # Cycle 2: D-E-F
}

print("Strongly Connected Components:")
print(strongly_connected_components(graph))


