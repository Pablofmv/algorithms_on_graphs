def strongly_connected_components(graph):

    #S1: Build the reverse graph:
    reverse_graph = {}

    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in reverse_graph:
                reverse_graph[neighbor] = []
            reverse_graph[neighbor].append(node)

        if node not in reverse_graph:
            reverse_graph[node] = []
    
    #S2: DFS in the reverse graph to get post-order number:

    postorder = {}
    visited_reverse = {}
    time = 1

    def dfs_reverse(v):
        nonlocal time
        visited_reverse[v] = True
        for neighbor in reverse_graph[v]:
            if neighbor not in visited_reverse:
                dfs_reverse(neighbor)
        postorder[v] = time
        time += 1
    
    for v in reverse_graph:
        if v not in visited_reverse:
            dfs_reverse(v)
    
    #S3: Run DFS in original graph in reverse port-order:

    visited_original = {}
    sccs = []

    def dfs_original(v, component):
        visited_original[v] = True
        component.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited_original:
                dfs_original(neighbor, component)
    
    for v in sorted(postorder, key = postorder.get, reverse = True):
        if v not in visited_original:
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
    
    


