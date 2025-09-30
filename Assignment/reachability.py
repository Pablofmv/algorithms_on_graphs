import sys
sys.setrecursionlimit(10**6)

def reach(adj, x, y):
    visited = [False] * len(adj)
    def dfs(v):
        visited[v] = True
        for nbr in adj[v]:
            if not visited[nbr]:
                dfs(nbr)
    dfs(x)
    return 1 if visited[y] else 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        adj[a].append(b)
        adj[b].append(a)
    x, y = map(int, input().split())
    print(reach(adj, x - 1, y - 1))