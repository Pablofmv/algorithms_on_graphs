def bellman_ford(graph, start):

    dist = {}
    prev = {}

    for node in graph:
        dist[node] = float("inf")
        prev[node] = None
    dist[start] = 0

    for _ in range(0, len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    prev[v] = u
    
    for u in graph:
        for v in graph[v]:
            if dist[v] > dist[u] + graph[u][v]:
                return None, None
    
    return dist, prev

def construct_path(prev, start, target):

    path = []
    u = target

    while u:
        path.append(u)
        u = prev[u]
    
    path.reverse()

    if path[0] != start:
        return None
    
    return path


graph = {
    'A': {'B': 4, 'D': 5},
    'B': {'C': 3},
    'C': {'B': 2},    # optional to show update propagation
    'D': {'C': -6}
}

dist, prev = bellman_ford(graph, 'A')

if dist and prev:
    print("Shortest distances:", dist)
    print("Paths:")
    for node in graph:
        if node != 'A':
            path = construct_path(prev, 'A', node)
            print(f"A → {node}: {path}, total cost = {dist[node]}")