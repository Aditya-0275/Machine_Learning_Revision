import numpy as np

# a1 = np.array([1, 2, 3])    # 1D array
# a2 = np.array([[1, 2], [3, 4]]) # 2D array
# a3 = np.array([[[1, 2], [3, 4]],    # 3D array
#                [[5, 6], [7, 8]]])

# print(a1)
# print(a2)
# print(a3)

# a0 = np.zeros((3, 3))
# a1  = np.ones((2, 2))
# ar  = np.arange(0, 10, 2)

# print(a0)
# print(a1)
# print(ar)

# a1 = np.array([10, 20, 30, 40, 50])
# print(a1[2])      # single element
# print(a1[-1])     # last element

# a2 = np.array([[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]])
# print(a2[1, -1])  

# a = np.array([10, 20, 30, 40, 50, 60])
# idx = np.array([1, 3, 5])

# print(a[idx])       # integer indexing

# cond = a > 30
# print(a[cond])      # boolean indexing

# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])


# print(x + y)    # add
# print(x - y)    # subtract
# print(x * y)    # multiply
# print(x / y)    # divide

# dtype = [('name', 'S10'), ('year', int), ('cgpa', float)]
# vals  = [('Hrithik', 2009, 8.5),
#          ('Ajay',    2008, 8.7),
#          ('Pankaj',  2008, 7.9),
#          ('Aakash',  2009, 9.0)]

# a = np.array(vals, dtype=dtype)

# print(np.sort(a, order='name'))
# print(np.sort(a, order=['year', 'cgpa']))

# print(np.exp(1))

# Creating a 2D NumPy array
# arr = np.array([[1, 2, 3],
#                 [4, 'Madhav', 5.0]], dtype = object)

# print("Array type:", type(arr))
# print("Number of dimensions:", arr.ndim)
# print("Shape:", arr.shape)
# print("Size:", arr.size)
# print("Element data type:", arr.dtype)

# x, y = input("Enter two numbers space separated: ").split()

# print(f"x: {x}\ny: {y}")

# arr = [[0]*int(y) for i in range(int(x))]

# for i in range(int(x)):
#     for j in range(int(y)):
#         arr[i][j] = int(input())
# n_arr = np.array(arr)

# print(n_arr.ndim)
# print(n_arr.shape)
# print(n_arr)

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(matrix[1][2])

# arr = np.array([1, 2, 3, 4, 5, 6])

# arr_2d = arr.reshape(2, 3)
# print(arr_2d)

# arr = np.array([[7, 8, 9], [10, 11, 12]])

# res = np.stack([arr, arr_2d], axis=0)
# print(res.shape)
