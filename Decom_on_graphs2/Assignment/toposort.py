#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    pass


def dfs(adj, used, order, x):
    used[x] = 1
    for v in adj[x]:
        if not used[v]:
            dfs(adj, used, order, v)
    order.append(x)  # postorder

def toposort(adj):
    used = [0] * len(adj)
    order = []
    for v in range(len(adj)):
        if not used[v]:
            dfs(adj, used, order, v)
    order.reverse()
    return order

if __name__ == '__main__':
    # --- minimal fix: support both interactive and redirected input ---
    if sys.stdin.isatty():
        lines = []
        while True:
            try:
                line = input()
                if not line:
                    break
                lines.append(line)
            except EOFError:
                break
        data = list(map(int, " ".join(lines).split()))
    else:
        data = list(map(int, sys.stdin.read().split()))
    # ------------------------------------------------------------------

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

