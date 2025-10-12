#Uses python3

import sys


def acyclic(adj):
    n = len(adj)
    visited = [False] * n
    rec_stack = [False] * n  # nodes on current DFS path

    def dfs(u):
        visited[u] = True
        rec_stack[u] = True
        for v in adj[u]:
            if not visited[v]:
                if dfs(v):
                    return True
            elif rec_stack[v]:
                return True
        rec_stack[u] = False
        return False

    for u in range(n):
        if not visited[u] and dfs(u):
            return 1
    return 0

if __name__ == '__main__':
    # ---- minimal change: smarter input handling ----
    if sys.stdin.isatty():  # interactive run
        first = input().split()
        n, m = map(int, first)
        rest = []
        for _ in range(m):
            rest.extend(input().split())
        data = list(map(int, first + rest))
    else:  # redirected/pipe
        data = list(map(int, sys.stdin.read().split()))
    # ------------------------------------------------

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
