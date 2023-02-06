import sys
from math import inf

def dijkstra(graph, start, end):
    distances = {node: inf for node in graph}
    distances[start] = 0
    unvisited = set(graph)
    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current)
        if current == end:
            break
        for neighbor, weight in graph[current].items():
            if weight + distances[current] < distances[neighbor]:
                distances[neighbor] = weight + distances[current]
    return distances[end]

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {},
}

start = 'A'
end = 'D'

shortest_distance = dijkstra(graph, start, end)
print(f"The shortest distance from {start} to {end} is {shortest_distance}")
