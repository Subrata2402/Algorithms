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