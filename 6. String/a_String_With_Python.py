"""
Given three strings
a = "hello"
b = "b2b2b2"
c = "3g3g"
"""

a = "hello"
b = "b2b2b2"
c = "3g3g"

# 1) Declare a new variable `d` and concatenate (a, b, c)
d = a + b + c
print("Concatenated string:", d)

# 2) Find the length of `d` and print `d[:-3]`
print("Length of d:", len(d))
print("d[:-3]:", d[:-3])

# 3) Check "a2" is present in `d`
print('"a2" is present in d:', "a2" in d)

# 4) Perform the following operation upper, lower, title, strip(), isdigit, find("3g"), capitalize, isalnum(), count("b2"), split(), swapcase, tstrip(), replace("hello" with "python")
print("Uppercase:", d.upper())
print("Lowercase:", d.lower())
print("Titlecase:", d.title())
print("Strip:", d.strip())
print("Is digit:", d.isdigit())
print("Find '3g':", d.find("3g"))
print("Capitalize:", d.capitalize())
print("Is alphanumeric:", d.isalnum())
print("Count 'b2':", d.count("b2"))
print("Split:", d.split())
print("Swapcase:", d.swapcase())
print("Replace 'hello' with 'python':", d.replace("hello", "python"))