# n = int(input("Enter a number :"))

# match n:
# 	case 4:
# 		print("Yes, you are right!")
# 	case 5 if n == 25:
# 		print("Yes, this is 5!")
# 	case _:
# 		print("Subrata Das!")
"""
print("Hello World!"); print("Subrata")
if (5 > 2):
	print("This is True")
	print(75)
if 4 == 4:
	print(4)
"""
# print(34)
# _namkj5465fjak = "Subrata"
# name = 546.45465
# NAME = "Subrata"
# Name = "Subrata"
# nAmE = "Subrata"
# print(_namkjdfjak)
# print(NAME)
# print(Name)
# print(name)
# print(nAmE)
# name, roll, Class = "Subrata", 21, "Msc"
# print(name)
# print(roll)
# print(Class)
# print("Name :", name)
# print(name, roll, Class, sep="\n")

# def factorial(number: str) -> str:
# 	"""Calculate the factorial of the given number.""" # This string is called Docstring
# 	if number == 0 or number == 1:
# 		return 1
# 	else:
# 		return number * factorial(number - 1)
# 	print(type(number))
# 	return 4

# print(factorial(5))
# print(factorial.__doc__)

# print("hello world")
# name = "Subrata"
# age = 22
# print(name) if age > 18 else print("Not Found") if age != 18 else print("subrata")

# if age > 18:
# 	print(name)
# else:
# 	if age != 18:
# 		print("Not Found")
# 	else:
# 		print("subrata")

# def knapsack(w, wt, value, n):
#     if n == 0 or w == 0:
#         return 0
#     if wt[n] > w:
#         return knapsack(w, wt, value, n-1)
#     else:
#         return max(value[n] + knapsack(w - wt[n], wt, value, n - 1), knapsack(w, wt, value, n - 1))

# w = 10
# wt = [5, 4, 6, 3]
# value = [10, 40, 30, 50]
# n = len(wt) - 1
# result = knapsack(w, wt, value, n)
# print("The max value is :", result)

# print([0]*4)
# print(5//2)
# new_str, count = "", 0
# string = "pwwkew"
# for i in string:
# 	if i not in new_str:
# 		new_str += i
# 	else:
# 		new_str = new_str[new_str.index(i) + 1:] + i
# 	if len(new_str) >= count:
# 		count = len(new_str)

# print(count)

# import numpy as np

# print(np.array([1, 2, 3]))

# Implement merge sort algorithm
def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]
		merge_sort(left)
		merge_sort(right)
		i, j, k = 0, 0, 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1
	return arr

arr = [4, 2, 6, 5, 3, 9, 1, 0, 8, 7]
print("The sorted array is :", merge_sort(arr))