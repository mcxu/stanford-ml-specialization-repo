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

