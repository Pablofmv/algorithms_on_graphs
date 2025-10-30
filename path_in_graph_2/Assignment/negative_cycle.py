#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    n = len(adj)
    dist = [0] * n

    for _ in range(0, len(adj) - 1):
        for u in range(0, len(adj)):
            for i, v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
    
    for u in range(0, len(adj)):
        for i,v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                return 1
    return 0


def main():
    # Read number of vertices and edges
    n, m = map(int, input().split())

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]

    # Read m edges (a, b, w)
    for _ in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    print(negative_cycle(adj, cost))


if __name__ == "__main__":
    main()
