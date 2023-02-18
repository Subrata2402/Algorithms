# Tail Recursive

def factorial(n, accumulator):
	if n == 0 or n == 1:
		return accumulator
	return factorial(n - 1, n * accumulator)

n = int(input("Enter a number : "))
print(f"The factorial of {n} is : {factorial(n, 1)}")

# Success