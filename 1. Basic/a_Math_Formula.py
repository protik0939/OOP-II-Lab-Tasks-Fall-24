"""
Create a function that will take 2 inputs from keyboard and perform the following formula:
    (a+b)^2 = a^2 + b^2 + 2ab
take input (a,b)
return a^2 + b^2 + 2ab
"""

def formula(a,b):
    return a**2 + b**2 + 2*a*b

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

print (f"(a+b)^2 = a^2 + b^2 + 2ab = {formula(a,b)}")