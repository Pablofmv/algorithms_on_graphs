from collections import deque

def bfs(graph, start):

    dist = {}
    for node in graph:
        dist[node] = float("inf")
    dist[start] = 0

    q = deque([start])

    while q:
        node = q.popleft()

        for v in graph[node]:
            if dist[v] == float("inf"):
                q.append(v)
                dist[v] = dist[node] + 1
            
    return dist

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS from node 'A'
distances = bfs(graph, 'A')

for node, d in distances.items():
    print(f"Distance from A to {node}: {d}")





