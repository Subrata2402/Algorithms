# Merge sort with devide and conquer

def merge(arr, low, middle, high):
	n1 = middle - low + 1
	n2 = high - middle
	Left = [0] * (n1)
	Right = [0] * (n2)
	for i in range(n1):
		Left[i] = arr[low + i]
	for j in range(n2):
		Right[j] = arr[middle + 1 + j]
	i, j, k = 0, 0, low
	while i < n1 and j < n2:
		if Left[i] <= Right[j]:
			arr[k] = Left[i]
			i += 1
		else:
			arr[k] = Right[j]
			j += 1
		k += 1
	
	while i < n1:
		arr[k] = Left[i]
		i += 1
		k += 1
	
	while j < n2:
		arr[k] = Right[j]
		j += 1
		k += 1

def merge_sort(arr, low, high):
	if low < high:
		middle = low + (high - low)//2
		merge_sort(arr, low, middle)
		merge_sort(arr, middle + 1, high)
		merge(arr, low, middle, high)

arr = [4, 2, 6, 5, 3, 9, 1, 0, 8, 7]
merge_sort(arr, 0, len(arr) - 1)
print("The sorted array is :", arr)

# Success