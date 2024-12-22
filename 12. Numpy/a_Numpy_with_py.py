"""
given a list
Score = [85, 90, 78, 92, 88]
"""
import numpy as np

Score = [85, 90, 78, 92, 88]

# a) Convert the data type into float
np_score = np.array(Score, dtype=float)
print("Scores as float:", np_score)

# b) Create a copy of "Score" named "a_score" and add 6 points on it.
a_score = np_score.copy() + 6
print("Original Score:", np_score)
print("Updated a_score:", a_score)

# c) Find shape, ndim, size, itemsize, dtype, and sort
print("Shape:", np_score.shape)
print("Number of dimensions (ndim):", np_score.ndim)
print("Size (number of elements):", np_score.size)
print("Item size (bytes per element):", np_score.itemsize)
print("Data type (dtype):", np_score.dtype)
print("Sorted scores:", np.sort(np_score))

# d) Find the index of scores greater than 80
indices = np.where(np_score > 80)
print("Indices of scores > 80:", indices[0])

# e) Find min, max, std, var, sum, mean
print("Minimum score:", np_score.min())
print("Maximum score:", np_score.max())
print("Standard Deviation:", np_score.std())
print("Variance:", np_score.var())
print("Sum of scores:", np_score.sum())
print("Mean of scores:", np_score.mean())

# f) Print slices of the array
print("Score[::2]:", np_score[::2])
print("Score[-3:-1]:", np_score[-3:-1])
print("Score[1:4]:", np_score[1:4])