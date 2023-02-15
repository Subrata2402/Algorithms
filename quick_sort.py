# Quick sort with devide and conquer

def quick_sort(arr, low, high):
	if low < high:
		pivot = partition(arr, low, high)
		quick_sort(arr, low, pivot - 1)
		quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return (i + 1)

arr = [4, 2, 6, 5, 3, 9, 1, 0, 8, 7]
quick_sort(arr, 0, len(arr) - 1)
print("The sorted array is :", arr)

# Success