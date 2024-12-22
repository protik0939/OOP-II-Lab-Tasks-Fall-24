"""
(a+b)^2 = a^2 + b^2 + 2ab
Use lambda function to perform above formula
"""

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
square_formula = lambda a, b: a**2 + b**2 + 2*a*b
print(f"Result: {(a + b)**2} = {square_formula(a, b)}")
