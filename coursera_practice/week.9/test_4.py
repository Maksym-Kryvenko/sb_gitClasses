import numpy as np

f_in = np.loadtxt('res.txt')
print(f_in)

ar = np.arange(1, 6, 1)
print(ar)

merged = np.vstack((f_in, ar))
print(merged)

print(np.max(merged), np.min(merged))

print(np.sum(merged, axis=0))

np.savetxt('res1.txt', ar)
