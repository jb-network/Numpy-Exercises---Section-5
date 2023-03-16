# Numpy Exercises - Section 5
# These are end of chapter exercises for the course: "Python for Data Science and Machine Learning Bootcamp"
# This is my personal approach the course method my differ

# 1 Import NumPy as np
import numpy as np

# 2 Create an array of 10 zeros
zero_array = np.zeros(10)
print(zero_array)

# 3 Create an array of 10 ones
ones_array = np.ones(10)
print(ones_array)

# 4 Create an array of 10 fives
fives_array = np.repeat(5, 10)
print(fives_array)

# 5 Create an array of integers from 10 to 50
a_range_array = np.arange(10, 51)
print(a_range_array)

# 6 Create an array of all the even integers from 10 to 50
even_range_array = np.arange(10, 51, 2)
print(even_range_array)

# 7 Create a 3x3 matrix with values ranging from 0 to 8
three_by_three = np.eye(3)
print(three_by_three)

# 8 Use Numpy to generate a random number between 0 and 1
rnd_num_1 = np.random.rand(1)
print(rnd_num_1)

# 9 Use NumPy to generate an array of 25 random number sample from a standard normal distribution
rnd_sample_1 = np.random.normal(0, 1, 25)
print(rnd_sample_1)

# 10 Create a matrix that matches the one provided on the exercise output
match_matrix = np.linspace(0.01, 1, 100).reshape((10, 10))
print(match_matrix)

# 11 Create an array of 20 linearly spaced points between 0 and 1:
spaced_points = np.linspace(0, 1, 20)
print(spaced_points)

# Numpy Indexing and Selection
# Mirror the matrix outputs provided

# 12 - Baseline matrix to use on next questions
match_matrix_1 = np.arange(1, 26).reshape(5, 5)
print(match_matrix_1)

# 13 2D 12-15, 17-20, 22-25, match into a 2D array
match_matrix_2 = match_matrix_1[2:5, 1:]
print(match_matrix_2)

# 14 Select 20 from the 2D matrix above, match into a single number
match_matrix_3 = match_matrix_1[3, 4]
print(match_matrix_3)

# 15 Select2,7,12 from the 2D martix above, match into a 2D array
match_matrix_4 = match_matrix_1[0:3, 1].reshape(-1, 1)
print(match_matrix_4)

# 16 Select 21 - 25 from the 2D martix above into a 1D array
match_matrix_5 = match_matrix_1[4]
print(match_matrix_5)

# 17 Select 16 - 20, 21 - 25 into a 2D array
match_matrix_6 = match_matrix_1[3:5]
print(match_matrix_6)

# 18 Get the sum of all the values in match_matrix_1
matrix_sum = np.sum(match_matrix_1)
print(matrix_sum)

# 19 Get the standard deviation of the values in match_matrix_1
matrix_std = np.std(match_matrix_1)
print(matrix_std)

# 20 Get the sum of all the columns in match_matrix_1
matrix_col_sum = np.sum(match_matrix_1, axis=0)
print(matrix_col_sum)
