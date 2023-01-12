# Returns the maximum value that can be put in a knapsack of capacity W

def knapsack(w, wt, value, n):
	if n == 0 or w == 0:
		return 0
	
	# If the weight of the nth item is more than the knapsack capacaity,
	# then this item cannot be included in the optimal solution
	if wt[n] > w:
		return knapsack(w, wt, value, n - 1)

	# Returns the maximum of two cases
	# Case 1: nth item included
	# Case 2: nth item not included

	else:
		return max(value[n] + knapsack(w - wt[n], wt, value, n - 1), knapsack(w, wt, value, n - 1))

w = 10
wt = [5, 4, 6, 3]
value = [10, 40, 30, 50]
n = len(wt) - 1
result = knapsack(w, wt, value, n)
print("The maximum value :", result)

# Success