import numpy as np

# 建立一維陣列
a = np.array([1, 2, 3, 4, 5])
b = np.empty((5,))
c = np.zeros((5,))
d = np.ones((5,))

# 建立二維陣列
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.empty((2,3))
# c = np.zeros((2,3))
# d = np.ones((2,3))

# 建立三維陣列
# a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# b = np.empty((2, 2, 3))
# c = np.zeros((2, 2, 3))
# d = np.ones((2, 2, 3))

print(a)
print(a.shape)
print(b)
print(b.shape)
print(c)
print(c.shape)
print(d)
print(d.shape)