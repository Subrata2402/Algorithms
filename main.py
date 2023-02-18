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

# import math
# a = 2

# for i in range(999):
# 	a = a*2

# print(a)

# from numerize import numerize
# print(numerize.numerize(a))

# Python for RSA asymmetric cryptographic algorithm.
# For demonstration, values are
# relatively small compared to practical application

# Implement Diffie-Hellman algorithm in Python.

# Python program to demonstrate
# Diffie-Hellman algorithm

# import math
# import random

# # a is sender private key
# # b is receiver private key
# a = random.randint(1, 10)
# b = random.randint(1, 10)

# print("Private key of sender a : ", a)
# print("Private key of receiver b : ", b)

# # P is a large prime number
# P = 23

# # G is a primitive root of P
# G = 9

# print("The value of P : ", P)
# print("The value of G : ", G)

# # gets the generated key
# x = int(math.pow(G, a) % P)
# y = int(math.pow(G, b) % P)

# print("Secret key for the sender is : ", x)
# print("Secret Key for the receiver is: ", y)

# # Secret key for sender
# ka = int(math.pow(y, a) % P)

# # Secret key for receiver
# kb = int(math.pow(x, b) % P)

# print("Secret key for the sender is : ", ka)
# print("Secret Key for the receiver is: ", kb)

# This code is contributed by
# Subrata Das

import openai

openai.api_key = "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"

prompt = input("Enter your prompt : ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# print(response)
print(response["choices"][0]["text"], "\n\n")