import numpy as np
l = []
for i in range(5):
    print("Enter the ", i + 1, "th element: ")
    x = int(input())
    l.append(x)
arr = np.array(l)
print(arr)

count = {}
for j in arr:
    if j in count:
        count[j] += 1
    else:
        count[j] = 1
for key, value in count.items():
    print(f"{key}: {value}")