# Matrix Chain Multiplication with recursive implemention
from math import inf as infinite

def matrix_chain_order(p, i, j):
	if i == j:
		return 0
	minCount = infinite
	for k in range(i, j):
		count = (matrix_chain_order(p, i, k)
		+ matrix_chain_order(p, k + 1, j)
		+ p[i - 1] * p[k] * p[j])
		if count < minCount:
			minCount = count
	return minCount

# 4 matrices of order 5x4, 4x6, 6x2, 2x7
order = [5, 4, 6, 2, 7]
n = len(order)
print("Minimum number of multiplication :", matrix_chain_order(order, 1, n - 1))

# Success