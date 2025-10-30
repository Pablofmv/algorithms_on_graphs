#Uses python3

import sys
import queue
import heapq


def distance(adj, cost, s, t):
    #write your code here
    
    n = len(adj)
    dist = [float("inf")] * n
    dist[s] = 0
    
    pq = [(0,s)]
    heapq.heapify(pq)

    while pq:

        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for i, v in enumerate(adj[u]):
                w = cost[u][i]
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))


    return dist[t] if dist[t] != float("inf") else -1


def main():
    # Read number of nodes and edges
    n, m = map(int, input().split())

    # Initialize adjacency and cost lists
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]

    # Read edges
    for _ in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    # Read start and end nodes
    s, t = map(int, input().split())

    # Compute and print result
    print(distance(adj, cost, s - 1, t - 1))


if __name__ == "__main__":
    main()