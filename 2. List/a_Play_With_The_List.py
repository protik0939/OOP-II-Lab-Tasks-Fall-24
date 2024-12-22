"""
a list is given -> a = [1, 3, 5, 7, 4]
"""
a = [1, 3, 5, 7, 4]

# 1) access a[-2], a[2]
print(a[-2])
print(a[2]) 

# 2) find the length and type
print(len(a))
print(type(a))

# 3) change a[-3] = 50, a[2:4]
a[-3] = 50
print(a[-3])
a[-3] = a[2:4]
print(a)

# 4) add 100 in last index
a.append(100)
print(a)

# 5) Join a new list [2, 4, 6] with a
a.extend([2, 4, 6])
print(a)

# 6) copy all values in a new list b
b = a.copy()
print(b)

# 7) sort the elements of b
b.sort()
print(b)

# 8) print all the elements using loop and break if get 5
for item in a:
    if item == 5:
        break
    print(item)

# 9) Find the largest number in a
print(max(a))