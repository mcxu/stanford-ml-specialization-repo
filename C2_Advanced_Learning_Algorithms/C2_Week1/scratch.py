import numpy as np

W = np.array([
    [1, -3, 5],
    [2, 4, 6]
])
print("W.shape: ", W.shape)
print("W transpose: ", W.T)

j = 0
w = W[:,0]
print("w at j={j}: ", w)

# ================= Matrix Multiplication Rules =================

A = np.array([
    [200],
    [17]
])

b = np.array([[-1, 1, 2]])

test1 = A * W
print("test1:\n", test1)

test2 = np.matmul(A.T, W)
print("test2:\n", test2)

test3 = A.T @ W
print("test3:\n", test3)

assert np.array_equal(test2, test3)