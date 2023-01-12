# Find longest commong subsequence with recursion

def lcs(str1, str2, m, n):
	if m == 0 or n == 0:
		return 0
	if str1[m - 1] == str2[n - 1]:
		return 1 + lcs(str1, str2, m - 1, n - 1)
	else:
		return max(lcs(str1, str2, m, n - 1), lcs(str1, str2, m - 1, n))

str1 = "abcbcdba"
str2 = "abcbad"
m = len(str1)
n = len(str2)
print("Length of LCS :", lcs(str1, str2, m, n))

# Success