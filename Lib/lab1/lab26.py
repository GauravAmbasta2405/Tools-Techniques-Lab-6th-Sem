import numpy as np
l = []
print("Enter the elements: ")
for i in range(5):

    x = int(input())
    l.append(x)
arr = np.array(l)
print(arr)

for i in range(0, 5):
    for j in range(i + 1, 5):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("Array after sorting: ")
for i in range(0, 5):
    print(arr[i], end=" ")