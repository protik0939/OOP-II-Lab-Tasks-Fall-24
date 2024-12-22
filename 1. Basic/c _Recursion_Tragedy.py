"""
Define a recursion function that return the factorial of a number
example: n -> Take input
perform n!
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {n} is {factorial(n)}")
