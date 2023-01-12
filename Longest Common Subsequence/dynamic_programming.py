# Find Longest Common Subsequence with dynamic programming

def lcs(str1, str2, m, n):
	tab = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
	for i in range(0, m - 1):
		for j in range(0, n):
			if i == 0 or j == 0:
				tab[i][j] = 0
			elif str1[i - 1] == str2[j - 1]:
				tab[i][j] = tab[i - 1][j - 1] + 1
			else:
				tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])
	indexL = tab[m][n]
	L = [0 for _ in (indexL + 1)]
	L[indexL] = "\0"
	indexM, indexN = m, n

	while indexM > 0 and indexN > 0:
		if str1[indexM - 1] == str2[indexN - 1]:
			L[indexL - 1] = tab[indexM - 1]
			indexM -= 1
			indexN -= 1
			indexL -= 1
		elif tab[indexM - 1][indexL] > tab[indexM][indexL - 1]:
			indexM -= 1
		else:
			indexN -= 1
	print("LCS of {} and {} is :".format(str1, str2), L)

str1 = "abcbcdba"
str2 = "abcbad"
m = len(str1)
n = len(str2)
lcs(str1, str2, m, n)

# Not Success