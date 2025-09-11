graph = {
    "A" : ["B"],
    "B" : ["A"],
    "C" : ["C","E"],
    "D" : ["C","E"],
    "E" : ["D"]
}

visited = {}

def explore(v):
    visited[v] = True
    print("Visited:", v)
    for nbr in graph[v]:
        if not visited.get(nbr, False):
            explore(nbr)

explore("C")

