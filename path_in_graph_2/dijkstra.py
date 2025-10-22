import heapq

def dijkstra(graph, start):

    dist = {}
    prev = {}

    for node in graph:
        dist[node] = float("inf")
        prev[node] = None
    dist[start] = 0

    pq = [(0, start)]
    heapq.heapify(pq)

    while pq:

        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                prev[v] = u
                heapq.heappush(pq, (dist[u] + graph[u][v], u))
    
    return dist, prev

def build_path(prev, target):

    path =[]
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    
    return list(reversed(path))

graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 7, 'E': 4},
    'D': {'B': 3, 'C': 7, 'E': 2},
    'E': {'C': 4, 'D': 2}
}

dist, prev = dijkstra(graph, 'A')
print(dist)
