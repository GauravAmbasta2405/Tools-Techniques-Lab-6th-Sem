import numpy as np
l = []
for i in range(5):
    print("Enter the ", i + 1, "th element: ")
    x = int(input())
    l.append(x)
arr = np.array(l)
print(arr)
max_element = np.max(arr)
print('Largest element in the given array: ', max_element)
