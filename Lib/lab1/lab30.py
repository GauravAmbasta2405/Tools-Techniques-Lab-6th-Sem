import numpy as np

arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
vertical = np.vstack((arr1, arr2))
horizontal = np.vstack((arr1, arr2))
for i in vertical:
    print(i)
print("\n")
for i in horizontal:
    print(i)