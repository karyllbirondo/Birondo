import numpy as np

# I. Creating Matrices
print("Initials: KAB -> [11, 1, 2] \nSecond letters of names: AA1 -> [1, 1, 9]")

# 1.a.i. 1st Matrix 
# Initials KAB: K=11, A=1, B=2
# Second letters of names AAI: A=1, A=1, I=9
matrix1 = np.array([[11, 1, 2], [1, 1, 9]])

matrix2 = np.array([[2, 0, 2], [6, 5, 2]])

# 1.b. Print both matrices
print("\nI. Printing both matrices:")
print("Matrix1:")
print(matrix1)
print("\nMatrix2:")
print(matrix2)

# II. Matrix Addition
print("\nII. Matrix Addition")

# 2.a. Add 1st and 2nd matrices to create 3rd matrix
matrix3 = matrix1 + matrix2

# 2.b. Print the 3rd matrix
print("\n2.b. Matrix3 (Sum of Matrix1 and Matrix2):")
print(matrix3)

# III. Scalar Multiplication
print("\nIII. Scalar Multiplication")

# 3.a. Multiply 1st matrix by a scalar value of 2
matrix4 = matrix1 * 2

# 3.b. Print the 4th matrix
print("\n3.b. Matrix4 (Matrix1 multiplied by 2):")
print(matrix4)

# IV. Matrix Transpose
print("\nIV. Matrix Transpose")

# 4.a. Create a transposed 5th matrix from the 2nd matrix
matrix5 = np.transpose(matrix2)

# 4.b. Print the 5th matrix
print("\n4.b. Matrix5 (Transpose of Matrix2):")
print(matrix5)

# V. Matrix Multiplication
print("\nV. Matrix Multiplication")

# 5.a. Multiply the 3rd matrix and 5th matrix to create a 6th matrix
matrix6 = np.matmul(matrix3, matrix5)

# 5.b. Print the 6th Matrix
print("\n5.b. Matrix6 (Product of Matrix3 and Matrix5):")
print(matrix6)

# VI. Sum of All Elements
print("\nVI. Sum of All Elements")

# 6.a. Calculate the sum of all elements in the 3rd matrix
sum_elements = np.sum(matrix3)

# 6.b. Print the sum
print("\n6.b. Sum of all elements in Matrix3:")
print(sum_elements)

# VII. Zero Matrix
print("\nVII. Zero Matrix")

# 7.a. Create a 2x3 zero matrix
matrix7 = np.zeros((2, 3))

# 7.b. Print the 7th matrix
print("\n7.b. Matrix7 (2x3 Zero Matrix):")
print(matrix7)