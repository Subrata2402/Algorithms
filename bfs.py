graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}

def breadth_first_search(node):
    visited = [False] * (len(graph))
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)

breadth_first_search('A')