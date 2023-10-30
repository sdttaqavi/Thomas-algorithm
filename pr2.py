#import library of time
import time
# define thomas algorithm
def thomas_algorithm(A, b):
    n = len(b)
    x = [0] * n
    # Decompose matrix A into matrix L and matrix U
    L = [0] * n
    U = [0] * n
    U[0] = A[0][0]
    for i in range(1, n):
        L[i] = A[i][i-1] / U[i-1]
        U[i] = A[i][i] - L[i] * A[i-1][i]
    # Solving Ly = b by using forward substitution
    y = [0] * n
    y[0] = b[0]
    for i in range(1, n):
        y[i] = b[i] - L[i] * y[i-1]
    # Solving Ux = y by using backward substitution
    x[n-1] = y[n-1] / U[n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - A[i][i+1] * x[i+1]) / U[i]
    return x

n = 5000  # number of equations
d = 4     # diagonal element
o = -1    # off-diagonal element

# Create a tridiagonal matrix
A = [[0]*n for i in range(n)]
for i in range(n):
    A[i][i] = d
    if i > 0:
        A[i][i-1] = o
    if i < n-1:
        A[i][i+1] = o

# Create vector b
b = [1 if i % 2 == 0 else -1 for i in range(n)]

# start time
start_time = time.perf_counter()

#find different variables of X
x = thomas_algorithm(A, b)

#round value of x up to 4 digit
rounded_x = [round(x, 4) for x in x]

print('x =', rounded_x)

# end time
end_time = time.perf_counter()
runtime = end_time - start_time
print("RUN time:", runtime, "seconds")
