import heapq

def dijkstra(graph, start):

    dist = {}
    prev = {}

    for node in graph:
        dist[node] = float("inf")
        prev[node] = None
    dist[start] = 0

    pq = [(0,start)]
    heapq.heapify(pq)

    while pq:

        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                prev[v] = u
                heapq.heappush(pq, (dist[v],v))
    
    return dist, prev

def build_path(prev, start, target):

    path = []
    cur = target
    
    while cur:
        path.append(cur)
        cur = prev[cur]
    
    path.reverse()

    if path[0] != start:
        return None
    
    return path

graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 7, 'E': 4},
    'D': {'B': 3, 'C': 7, 'E': 2},
    'E': {'C': 4, 'D': 2}
}

dist, prev = dijkstra(graph, 'A')
print(dist)

