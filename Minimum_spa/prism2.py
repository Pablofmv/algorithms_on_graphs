import heapq

def prim(n, edges, start =0):
    
    graph = {i : [] for i in range(0,n)}
    for u, v, w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    INF = float("inf")
    cost = [INF] * n
    parent = [-1] * n
    cost[start] = 0

    pq = [(cost[i],i) for i in range(0,n)]
    heapq.heapify(pq)

    in_mst = [False] * n
    mst = []

    while pq:

        w, u = heapq.heappop(pq)

        if in_mst[u]:
            continue

        in_mst[u] = True

        if parent[u] != -1:
            mst.append([parent[u],u, w])
        
        for v, w in graph[u]:
            if not in_mst[v] and w < cost[v]:
                cost[v] = w
                parent[v] = u

                heapq.heappush(pq,(cost[v], v))
    
    return mst

edges = [
    [0,1,1],
    [1,2,1],
    [2,3,2],
    [0,3,2],
    [0,4,3],
    [3,4,3],
    [1,4,6]
]

print(prim(5, edges, start=0))




