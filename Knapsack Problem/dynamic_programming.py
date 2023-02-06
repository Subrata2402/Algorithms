# Knapsack Problem with Dynamic Programming

def dynamic_0_1_knapsack(value, weight, n, total_weight):
	for w in range(total_weight):
		value[0][w] = 0
	for i in range(1, n):
		value[i][0] = 0
		for w in range(1, total_weight):
			if weight[i] > w:
				value[i][w] = value[i - 1][w]
				keep[i][w] = 0
			else:
				value[i][w] = max(value[i] + value[i - 1][w - w[i]], value[i - 1][w])
				keep[i][w] = 1

	# Print the selected items here
	k = total_weight
	for i in range(1, n):
		if keep[i][k] == 1:
			print(i)
			k = k - weight[i]

	return value[n][w]

