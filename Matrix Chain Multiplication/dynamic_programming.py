# Matrix Chain Multiplication with dynamic programming
from math import inf as infinite

def matrix_chain_order(p, n):
	m = [[0 for _ in range(n)] for _ in range(n)]
	s = [[0 for _ in range(n)] for _ in range(n)]

	for L in range(2, n):
		for i in range(1, n - L + 1):
			j = i + L - 1
			m[i][j] = infinite
			for k in range(i, j):
				count = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
				if count < m[i][j]:
					m[i][j] = count
					s[i][j] = k
	print("Minimum number of multiplication is :", m[1][n - 1])
	print("Order of multiplication is :")
	print_parenthesis(s, 0, n - 1)

def print_parenthesis(s, i, j):
	if i == j:
		print("M", i, sep="", end="")
	else:
		print("(", end="")
		print_parenthesis(s, i, s[i][j])
		print_parenthesis(s, s[i][j] + 1, j)
		print(")", end="")
	

# 4 matrices of order 5x4, 4x6, 6x2, 2x7
order = [5, 4, 6, 2, 7]
n = len(order)
matrix_chain_order(order, n - 1)

# Success