"""
a tuple is given -> a = (1, 3, 5, 7, 4)
"""

# Given tuple
a = (1, 3, 5, 7, 4)

# a) Find the sum of all odd numbers in `a`
sum_odd = sum(x for x in a if x % 2 != 0)
print("Sum of all odd numbers:", sum_odd)

# b) Find the sum of all odd index elements in `a`
sum_odd_index = sum(a[i] for i in range(1, len(a), 2))
print("Sum of all odd index elements:", sum_odd_index)

# c) Count the number of odd and even numbers separately
odd_count = sum(1 for x in a if x % 2 != 0)
even_count = sum(1 for x in a if x % 2 == 0)
print("Number of odd numbers:", odd_count)
print("Number of even numbers:", even_count)

# d) Extend the tuple with `(2, 4, 6)`
a_extended = a + (2, 4, 6)
print("Extended tuple:", a_extended)

# e) Add a new item `(400)` at index 2
a_list = list(a)
a_list.insert(2, 400)
a_modified = tuple(a_list)
print("Tuple after adding 400 at index 2:", a_modified)

# f) Remove the last element
a_list = list(a)
a_list.pop()
a_removed_last = tuple(a_list)
print("Tuple after removing the last element:", a_removed_last)

# g) Perform slicing `[-4:-1]`
sliced_tuple = a[-4:-1]
print("Sliced tuple:", sliced_tuple)

# h) Print the tuple using loop and use `continue` if the value is 5
for item in a:
    if item == 5:
        continue
    print(item, end=" ")
print()
