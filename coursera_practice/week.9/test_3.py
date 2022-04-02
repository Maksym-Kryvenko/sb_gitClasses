import numpy as np

# print(np.zeros(10))
# print(np.ones(11))
# print(np.empty(12))

# print(np.zeros((3, 4)))
# print(np.zeros((2, 4, 5)))

# print(np.arange(-10, 10, 0.1))

# print(np.eye(5))

mas = np.eye(5)

# for i in mas.flat:


for i in range(5):
    for j in range(5):
        if i < j:
            mas[i, j] = 2

np.savetxt('res.txt', mas)
