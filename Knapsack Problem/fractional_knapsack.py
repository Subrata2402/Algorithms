# Fractional Knapsack Problem using Greedy Algorithm

def fractional_knapsack(w, value, weight, n):
	index = list(range(n))
	ratio = [v / w for v, w in zip(value, weight)]
	index.sort(key=lambda i: ratio[i], reverse=True)
	max_value = 0
	for i in index:
		if weight[i] <= w:
			max_value += value[i]
			w -= weight[i]
		else:
			max_value += value[i] * (w / weight[i])
			break
	return max_value

w = 10
value = [10, 40, 30, 50]
weight = [5, 4, 6, 3]
n = len(value)
result = fractional_knapsack(w, value, weight, n)
print("The maximum value :", result)