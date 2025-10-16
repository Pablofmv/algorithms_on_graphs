from collections import deque

def bfs_short_path(graph, start):

    dist = {}
    prev = {}

    for node in graph:
        dist[node] = float("inf")
        prev[node] = None
    dist[start] = 0

    q = deque([start])

    while q:

        u = q.popleft()

        for v in graph[u]:
            if dist[v] == float("inf"):
                q.append(v)
                dist[v] = dist[u] + 1
                prev[v] = u
    
    return dist, prev

def reconstruct_path(start, target, prev):

    path = []
    u = target
    while u is not None:
        path.append(u)
        u = prev[u]
    
    path.reverse()

    if path[0] != start:
        return None
    
    return path

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Build shortest-path tree from 'A'
dist, prev = bfs_short_path(graph, 'A')

# Print distances
for node, d in dist.items():
    print(f"Distance from A to {node}: {d}")

# Reconstruct specific paths
target = 'F'
path = reconstruct_path('A', target, prev)
print(f"Shortest path from A to {target}: {path}")
