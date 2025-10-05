def strongly_connected_components(graph):

    #S1: Build the reverse_graph
    reverse_graph = {}
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in reverse_graph:
                reverse_graph[neighbor] = []
            reverse_graph[neighbor].append(node)
        if node not in reverse_graph:
            reverse_graph[node] = []
    
    #S2: DFS on Gr to postorder number
    visited_gr = {}
    postorder = {}
    time = 1

    def dfs_reverse(v):
        nonlocal time
        visited_gr[v] = True
        for neighbor in reverse_graph[v]:
            if neighbor not in visited_gr:
                dfs_reverse(neighbor)
        postorder[v] = time
        time += 1
    
    for v in reverse_graph:
        if v not in visited_gr:
            dfs_reverse(v)
    
    visited_g = {}
    sccs = []

    def dfs_original(v, component):
        visited_g[v] = True
        component.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited_g:
                dfs_original(neighbor, component)
    
    for v in sorted(postorder, key = postorder.get, reverse = True):
        if v not in visited_g:
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
