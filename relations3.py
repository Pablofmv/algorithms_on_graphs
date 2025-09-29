graph = {
    'u': ['v'],
    'v': ['w'],
    'w': ['u'],  # back edge (w -> u creates a cycle)
    'x': ['y'],
    'y': []
}

visited = {}
pre = {}
post = {}
clock = 1

def previsit(v):
    global clock
    pre[v] = clock
    print(f"Previsit ({v}) : {clock}")
    clock += 1

def postvisit(v):
    global clock
    post[v] = clock
    print(f"Postvisit ({v}) : {clock}")
    clock += 1

def explore(v):
    visited[v] = True
    previsit(v)
    for nbr in graph[v]:
        if not visited.get(nbr, False):
            explore(nbr)
    postvisit(v)

for v in graph:
    if not visited.get(v, False):
        explore(v)

print("Pre times:", pre)
print("Post time:", post)

def relation(u, v):
    if pre[u] < pre[v] and post[v] < post[u]:
        return f"{v} is nested inside {u}"
    elif post[u] < pre[v] or post[v] < pre[u]:
        return f"{v} and {u} are disjoint." 
    elif pre[v] < pre[u] and post[u] < post[v]:
        return f"Back edge detected: {u} -> {v}"
    else:
        return "Other case"

print(relation('u', 'v'))
print(relation('u', 'x'))
print(relation('w', 'u'))

