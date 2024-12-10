# https://www.codewars.com/kata/5819f1c3c6ab1b2b28000624
#
# Description:
# The Padovan sequence is the sequence of integers P(n) defined by the initial
# values
# P(0)=P(1)=P(2)=1
# and the recurrence relation
# P(n)=P(n-2)+P(n-3)
# The first few values of P(n) are
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200,
# 265, ...
# Task
# The task is to write a method that returns i-th Padovan number for i around
# 1,000,000
# Hint: use matrices

# from collections import OrderedDict
import pdb


# Function to multiply two 2x2 matrices
def multiply(mat1, mat2):

    # Perform matrix multiplication
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    # Update matrix mat1 with the result
    mat1[0][0], mat1[0][1] = x, y
    mat1[1][0], mat1[1][1] = z, w


# Function to perform matrix exponentiation
def matrix_power(mat1, n):

    # Base case for recursion
    if n == 0 or n == 1:
        return n

    # Initialize a helper matrix
    mat2 = [[1, 1], [1, 0]]

    # Recursively calculate mat1^(n // 2)
    matrix_power(mat1, n // 2)

    # Square the matrix mat1
    multiply(mat1, mat1)

    # If n is odd, multiply by the helper matrix mat2
    if n % 2 != 0:
        multiply(mat1, mat2)


# Function to calculate the nth Fibonacci number
def padovan(n):
    if n <= 2:
        return 1

    # Initialize the transformation matrix
    mat_m = [[1, 1], [1, 0]]

    # Raise the matrix mat1 to the power of (n - 1)
    matrix_power(mat_m, n - 1)

    # The result is in the top-left cell of the matrix
    return mat_m[0][0]


if __name__ == "__main__":
    n = 4
    result = padovan(n)
    print(result)


# print(padovan(n))
