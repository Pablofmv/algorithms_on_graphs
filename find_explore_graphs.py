graph = {
    "A" : ["B","C"],
    "B" : ["A","D"],
    "C" : ["A"],
    "D" : ["B"],
    "E" : ["F"],
    "F" : ["E"]
}

visited = {}
components = []

def explore(v, comp):

    visited[v] = True
    comp.append(v)
    for nbr in graph[v]:
        if not visited.get(nbr,False):
            explore(nbr,comp)

def find_components():

    for v in graph:
        if not visited.get(v, False):
            comp = []
            explore(v, comp)
            components.append(comp)

find_components()
print("Conected Components:", components)