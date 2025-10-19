def naive_shortest_path(graph, start):

    dist = {}
    prev = {}

    for node in graph:
        dist[node] = float("inf")
        prev[node] = None
    dist[start] = 0

    changed = True
    while changed:
        changed = False
        for u in graph:
            for v in graph[u]:
                if dist[v] > dist[u] + graph[u][v]:
                    changed = True
                    dist[v] = dist[u] + graph[u][v]
                    prev[v] = u
    
    return dist, prev

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'D': 2, 'E': 3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {},
    'E': {'D': 1}
}

dist, prev = naive_shortest_path(graph, 'A')
print(dist)
print(prev)