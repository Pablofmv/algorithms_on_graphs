graph = {
    "A": ["B", "C"],
    "B": [],
    "C": []
}

visited = {}
pre = {}
post = {}
clock = 1

def previsit(v):
    global clock
    pre[v] = clock
    print(f"Previsit({v}):{clock}")
    clock += 1

def postvisit(v):
    global clock
    post[v] = clock
    print(f"Postvisit({v}):{clock}")
    clock += 1

def explore(v):
    visited[v] = True
    previsit(v)
    for w in graph[v]:
        if not visited.get(w, False):
            explore(w)
    postvisit(v)

def dfs():
    for v in graph:
        if not visited.get(v, False):
            explore(v)

dfs()
print("Final Pre numbers", pre)
print("Final Post Numbers", post)

