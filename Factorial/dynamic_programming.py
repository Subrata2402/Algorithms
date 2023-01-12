# Factorial with dynamic programming

def fact_dp(n):
	if n >= 0:
		result[0] = 1
		for i in range(1, n + 1):
			result[i] = i * result[i - 1]
		return result[n]

n = 5
result = [0 for _ in range(n + 1)]
print(fact_dp(n))

# Success