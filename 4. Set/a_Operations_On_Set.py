"""
given two sets:
a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}
"""

a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}

# 1) Print `a`, `b`
print("Set a:", a)
print("Set b:", b)

# 2) Print length and their type
print("Length of a:", len(a))
print("Length of b:", len(b))
print("Type of a:", type(a))
print("Type of b:", type(b))

# 3) Add a new element `10` in set `a`
a.add(10)
print("Set a after adding 10:", a)

# 4) Remove `8` from the set `a`
a.discard(8)
print("Set a after removing 8:", a)

# 5) Perform set operations
print("Union of a and b:", a | b)
print("Intersection of a and b:", a & b)
print("Difference of a and b:", a - b)
print("Symmetric difference of a and b:", a ^ b)
print("Is b a subset of a?", b.issubset(a))

# 6) Join a new list `[2, 3, 4]` with set `a`
a.update([2, 3, 4])
print("Set a after joining with list:", a)