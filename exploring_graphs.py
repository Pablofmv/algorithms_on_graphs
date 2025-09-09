graph = {
    "A" : ["B"],
    "B" : ["A"],
    "C" : ["D"],
    "D" : ["C","E"],
    "E" : ["D"]
}

visited = {}

def explore(v):
    visited[v] = True
    print("Visited:",v)
    for nbr in graph[v]:
        if not visited.get(nbr, False):
            explore(nbr)

# Example 1: start from "C"
visited = {}
explore("C")
# Output order: C → D → E

# Example 2: start from "A"
visited = {}
explore("A")
# Output order: A → B
