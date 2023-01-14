# Merge sort with devide and conquer

from math import inf

def merge(arr, low, middle, high):
	n1 = middle - low + 1
	n2 = high - middle
	Left = [0] * (n1 + 1)
	Right = [0] * (n2 + 1)
	for i in range(1, n1):
		Left[i] = arr[low + i - 1]
	for j in range(1, n2):
		Right[j] = arr[middle + j]
	Left[n1 + 1] = inf
	Right[n2 + 1] = inf
	i, j = 1, 1
	for k in range(low, high):
		if Left[i] <= Right[j]:
			arr[k] = Left[i]
			i += 1
		else:
			arr[k] = Right[j]
			j += 1

def merge_sort(arr, low, high):
	if low < high:
		middle = (low + high)//2
		merge_sort(arr, low, middle)
		merge_sort(arr, middle + 1, high)
		merge(arr, low, middle, high)

arr = [4, 2, 6, 5, 3, 9, 1, 0, 8, 7]
merge_sort(arr, 1, len(arr))
print(arr)

# Not Success