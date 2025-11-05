def find(parent, x):

    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, rank, a, b):

    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA != rootB:

        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1
        
        return True
    
    return False

def kruskal(n, edges):

    edges.sort(key = lambda x: x[2])
    parent = list(range(n))
    rank = [0] * n
    mst = []

    for u,v,w in edges:
        if union(parent, rank, u, v):
            mst.append([u,v,w])
        
        if len(mst) == n - 1:
            break
    
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

n = 5  # number of nodes: 0,1,2,3,4
mst = kruskal(n, edges)
print(mst)
