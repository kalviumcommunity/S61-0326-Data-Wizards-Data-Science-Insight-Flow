import numpy as np

array_1d = np.array([1, 2, 3, 4])
array_2d = np.array([[10, 20, 30], [40, 50, 60]])

print('1D array:', array_1d)
print('2D array:\n', array_2d)

print('\n--- Shape ---')
print('shape of 1D array:', array_1d.shape)
print('This means 4 elements in a single row (1 row, 4 columns in 2D terms)')
print('shape of 2D array:', array_2d.shape)
print('This means 2 rows and 3 columns')

print('\n--- Dimensions (ndim) ---')
print('ndim of 1D array:', array_1d.ndim)
print('ndim of 2D array:', array_2d.ndim)
print('1D arrays have 1 dimension; 2D arrays have 2 dimensions for rows and columns')

print('\n--- Indexing 1D ---')
print('element at position 0:', array_1d[0])
print('element at position 2:', array_1d[2])

print('\n--- Indexing 2D ---')
print('element at row 0, col 0:', array_2d[0, 0])
print('element at row 0, col 2:', array_2d[0, 2])
print('element at row 1, col 1:', array_2d[1, 1])

print('\n--- Visualization logic ---')
print('2D array row 0:', array_2d[0])
print('2D array row 1:', array_2d[1])
print('2D array column 0:', array_2d[:, 0])
print('2D array column 2:', array_2d[:, 2])

print('\n--- Explanation ---')
print('Shape is a tuple of dimensions, like (rows, columns) for 2D arrays.')
print('ndim is the number of axes, 1 for a line of values, 2 for a grid of values.')
print('Indexing in 1D uses a single number for position; 2D indexing uses row and column.')

print('\n--- More examples ---')
print('last element in 1D array (negative index):', array_1d[-1])
print('second row of 2D array:', array_2d[1])
print('subarray from 2D: first two rows, last two cols:\n', array_2d[:, 1:3])

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print('\n3D array:', array_3d)
print('shape of 3D array:', array_3d.shape)
print('ndim of 3D array:', array_3d.ndim)

reshaped_2d = array_1d.reshape(2, 2)
print('\nreshaped from 1D to 2D:', reshaped_2d)
print('shape after reshape:', reshaped_2d.shape)

transposed_2d = array_2d.T
print('\ntransposed 2D array:\n', transposed_2d)
print('shape after transpose:', transposed_2d.shape)

stacked = np.vstack([array_2d, array_2d])
print('\nstacked 2D array (vertical):\n', stacked)
print('shape of stacked:', stacked.shape)

masked = array_2d[array_2d > 30]
print('\nboolean mask, values > 30:', masked)
print('shape of masked result:', masked.shape)

flat = array_2d.flatten()
print('\nflattened array:', flat)
print('shape of flattened:', flat.shape)

print('\n--- Advanced 2D indexing patterns ---')
print('first row, all cols:', array_2d[0, :])
print('all rows, second col:', array_2d[:, 1])
print('middle block from 2D (if available):\n', array_2d[0:2, 1:3])

print('\n--- Advanced explanation ---')
print('Reshape changes how items are grouped across dimensions but not content count.')
print('Transpose swaps rows and columns in 2D arrays.')
print('Boolean indexing picks elements that meet conditions, returning a 1D result.')

print('\n--- Run this script ---')
print('From terminal: python src/numpy_array_basics.py')
