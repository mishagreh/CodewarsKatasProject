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
# Python Program to find the Nth fibonacci number using
# Matrix Exponentiation

MOD = 10**9 + 7


# function to multiply two 2x2 Matrices
# def multiply(A, B):
#     # Matrix to store the result
#     C = [[0, 0], [0, 0]]
#
#     # Matrix Multiply
#     C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
#     C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
#     C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
#     C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
#
#     # Copy the result back to the first matrix
#     A[0][0] = C[0][0]
#     A[0][1] = C[0][1]
#     A[1][0] = C[1][0]
#     A[1][1] = C[1][1]

# Function to multiply two 3x3 matrices
def multiply(A, B):
    # Matrix to store the result
    C = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k] * B[k][j]

    # Copy the result back to the first matrix A
    for i in range(3):
        for j in range(3):
            A[i][j] = C[i][j]


# Function to find (Matrix M ^ expo)
def power(M, expo):
    # Initialize result with identity matrix
    ans = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    # breakpoint()

    # Fast Exponentiation
    while expo > 0:
        if expo & 1:
            multiply(ans, M)
        multiply(M, M)
        expo >>= 1

    return ans


def nthFibonacci(z):
    # Base case
    if z <= 2:
        return 1

    M = [
        [0, 1, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]

    # F(0) = 1, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 2, F(5) = 3
    # we took F(2) and F(1)
    F = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ]

    # Multiply matrix M (n - 2) times
    res = power(M, z - 2)

    # Multiply Resultant with Matrix F
    multiply(res, F)

    return res[0][0] % MOD


# Sample Input
z = 1_000_000

# Print the nth fibonacci number
print(f'{z}-th element:', nthFibonacci(z))
