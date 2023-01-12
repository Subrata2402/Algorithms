# Factorial with memoization

def fact_memo(aa):
	if aa == 0 or aa == 1:
		return 1
	else:
		if temp[aa] != 0:
			return temp[aa]
		else:
			temp[aa] = (aa * fact_memo(aa - 1))
			return temp[aa]

aa = 5
temp = [0 for _ in range(aa + 1)]
print(fact_memo(aa))

# Success