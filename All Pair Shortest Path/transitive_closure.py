# Transitive Closure of a Graph By Floyd-Warshall Algorithm

def transitive_closure(connected):
	v = len(connected[0])
	for k in range(v):
		for i in range(v):
			for j in range(v):
				connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])
	print("The transitive closure of the given graph is :")
	for i in range(v):
		for j in range(v):
			if i == j:
				print("1", end="  ")
			else: 
				print(connected[i][j], end="  ")
		print()

graph = [
	[1, 1, 0, 1],
	[0, 1, 1, 0],
	[0, 0, 1, 1],
	[0, 0, 1, 1]
]
transitive_closure(graph)

# Success