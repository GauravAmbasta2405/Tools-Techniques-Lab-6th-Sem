import numpy as np
l = []
for i in range(5):
    print("Enter the ", i + 1, "th element: ")
    x = int(input())
    l.append(x)
arr = np.array(l)
print(arr)
for i in range(0, 3):
    x = arr[0]
    for j in range(0, 4):
        arr[j] = arr[j + 1]
    arr[4] = x
for i in range(0, 5):
    print(arr[i], end=' ')