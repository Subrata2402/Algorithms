# Using a Python dictionary to act as an adjacency list

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()

def depth_first_search(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            depth_first_search(visited, graph, neighbour)

depth_first_search(visited, graph, 'A')