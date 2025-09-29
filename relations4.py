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
    print(f"Pre visit{v} : {clock}")
    pre[v] = clock
    clock += 1

def postvisit(v):
    global clock
    print(f"Post visit {v} : {clock}")
    post[v] = clock
    clock += 1

def explore(v):
    previsit(v)
    visited[v] = True
    for nbr in graph[v]:
        if not visited.get(nbr, False):
            explore(nbr)
    postvisit(v)

for v in graph:
    if not visited.get(v, False):
        explore(v)

print("Pre visit:", pre)
print("Post visit:", post)