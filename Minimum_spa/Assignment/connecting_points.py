#Uses python3
import sys
import math

def minimum_distance(x, y):
    n = len(x)

    def dist(i, j):
        return math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)

    key = [float('inf')] * n
    used = [False] * n
    key[0] = 0.0

    result = 0.0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not used[i] and (u == -1 or key[i] < key[u]):
                u = i

        used[u] = True
        result += key[u]

        for v in range(n):
            if not used[v]:
                d = dist(u, v)
                if d < key[v]:
                    key[v] = d

    return result


if __name__ == '__main__':
    n = int(input().strip())
    x = []
    y = []

    for _ in range(n):
        xi, yi = map(int, input().strip().split())
        x.append(xi)
        y.append(yi)

    print("{0:.9f}".format(minimum_distance(x, y)))
