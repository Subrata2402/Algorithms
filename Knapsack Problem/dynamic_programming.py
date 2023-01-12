def dynamic_0_1_knapsack(value, weight, n, total_weight):
	for w in range(total_weight):
		value[0][w] = 0
	for i in range(1, n):
		value[i][0] = 0
		for w in range(1, total_weight):
			if weight[i] > w:
				value[i][w] = value[i - 1][w]