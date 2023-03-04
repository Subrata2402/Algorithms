# def greet():
# 	print("hello")

# greet()

# def add(x, y):
#     c = x + y
#     return c

# result = add(5, 4)
# print(result)

# add = lambda a, b: a+b; print(add(4, 5))

# for i in range(1, 11):
#     print(i)

# i = 0
# n = 4
# while n == 4:
#     print(i)
#     i = i + 1
#     n = 2

# not tail recursion
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#     	return n * factorial(n - 1)

# n = 5
# print(f"The factorial of {n} is : {factorial(5)}")
# print("The factorial of {} is : {}".format(n, factorial(5)))
# print("The factorial of " + str(n) + " is : " + str(factorial(5)))
# print("The factorial of %d is : %d" % (n, factorial(5)))
# print("The factorial of", n, "is :", factorial(5))

# tail recursion

# def factorial(n, accumulator):
#     if n == 1 or n == 0:
#         return accumulator
#     else:
#         return factorial(n-1, n*accumulator)

# print(factorial(5, 1))