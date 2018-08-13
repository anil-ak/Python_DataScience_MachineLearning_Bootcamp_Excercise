# Import NumPy as np
import numpy as np
print np
print "Successfully imported numpy as np"

# Create an array of 10 zeros
print "Create an array of 10 zeros"
Zeros10_Array = np.zeros(10)
print Zeros10_Array

# Create an array of 10 ones
print "Create an array of 10 ones"
Ones10_Array = np.ones(10)
print Ones10_Array

# Create an array of 10 fives
print "Create an array of 10 fives"
Fives10_Array = np.full(10, 5)
print Fives10_Array

# Create an array of the integers from 10 to 50
print "Create an array of the integers from 10 to 50"
# Options Used: arange([start, ]stop, [step, ]dtype=None)
Range_of_numbers_array = np.arange(10, 50+1, 1)
print Range_of_numbers_array

# Create an array of all the even integers from 10 to 50
Range_of_even_numbers_array = np.arange(10, 50+1, 2)
print Range_of_even_numbers_array

# Create a 3x3 matrix with values ranging from 0 to 8
# np.arange(End+1).reshape(matrix size, size) or a = np.arange(End+1) && a.reshape(matrix size, size)
Matrix_3x3_range_array = np.arange(8+1).reshape(3, 3)
print Matrix_3x3_range_array

# Create a 3x3 identity matrix
Identity_Matrix = np.identity(3)
print Identity_Matrix

# Use NumPy to generate a random number between 0 and 1
Random_Number_Array = np.random.rand(1)
print Random_Number_Array

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
Random_Number__Range_Array = np.random.randn(25)
print Random_Number__Range_Array

'''
Create the following matrix:

array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
       [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
       [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
       [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
       [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
       [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
       [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
       [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
       [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
       [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])
'''
print "Create the following matrix:"
Range_under_number_Array = np.arange(0.01, 1.01, .01).reshape(10,10)
print Range_under_number_Array


# Create an array of 20 linearly spaced points between 0 and 1:
Range_linearly_spaced_Array = np.linspace(0,1,20)
print Range_linearly_spaced_Array
#####or
Range_linearly_spaced_Array = np.linspace(0,1,num=20, endpoint=True)
print Range_linearly_spaced_Array
Range_linearly_spaced_Array = np.linspace(0,1,num=20, endpoint=False)
print Range_linearly_spaced_Array


'''
Numpy Indexing and Selection
Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

mat = np.arange(1,26).reshape(5,5)

array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE

array([[12, 13, 14, 15],
       [17, 18, 19, 20],
       [22, 23, 24, 25]])

'''
mat = np.arange(1,26).reshape(5,5)
print "Given Matrix: "
print mat
print mat[2:, 1:]

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# 20
tmp_num = mat[3:4, 4:5]
print tmp_num

'''
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE

array([[ 2],
       [ 7],
       [12]])

'''
print mat[:3, 1:2]

'''
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE

array([21, 22, 23, 24, 25])
'''

print mat[4:5]

'''
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE

array([[16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])

'''
print mat[3:5]

'''
Now do the following
Get the sum of all the values in mat
325

'''
print np.sum(mat)

'''
Sum of elements of sub-array
'''
print np.sum(mat[3:5])

'''
Get the standard deviation of the values in mat
7.2111025509279782
'''
print np.std(mat)

'''
Get the sum of all the columns in mat

array([55, 60, 65, 70, 75])

'''
print np.sum(mat, axis=0)

'''
above sum, std can be used mat.sum or mat.std as well
'''



