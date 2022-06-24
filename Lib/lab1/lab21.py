import numpy as np

l = []
for i in range(5):
    print("Enter the ", i + 1, "th element: ")
    x = int(input())
    l.append(x)
arr = np.array(l)
print(arr)
x = int(input("enter the element you want to find the occurence: "))
count = 0
for i in range(len(arr)):
    if arr[i] == x:
        count = count + 1
print("Occurrence is:  ", count)