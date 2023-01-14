# All Pair Shortest Path Program (Floyd-Warshall)
from math import inf

def all_pair_shortest_path(dist: list[list]) -> None:
	"""Find the all pair shortest path."""
	v = len(dist[0])
	for k in range(v):
		for i in range(v):
			for j in range(v):
				if dist[i][j] > dist[i][k] + dist[k][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
	print("Shortest distances between every pair of vertices :")
	for i in range(v):
		for j in range(v):
			if dist[i][j] == inf:
				print("INF", end="  ")
			else:
				print(dist[i][j], end="  ")
		print()

graph = [
	[0, inf, 3, inf],
	[2, 0, inf, inf],
	[inf, 6, 0, 1],
	[5, inf, inf, 0]
]
all_pair_shortest_path(graph)

# Success