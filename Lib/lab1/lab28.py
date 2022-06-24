import numpy as np
l = []
print("Enter the 1st array elements: ")
for i in range(3):

    x = int(input())
    l.append(x)
arr1 = np.array(l)
print(arr1)
l = []
print("Enter the 2st array elements: ")
for i in range(3):
    x = int(input())
    l.append(x)
arr2 = np.array(l)
print(arr2)

c = np.concatenate((arr1, arr2), axis=0)
print(c)