import numpy as np
def binary_search(array, n):
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < n:
            low = mid + 1

        elif array[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1
l = []
print("Enter the elements: ")
for i in range(5):
    x = int(input())
    l.append(x)
arr = np.array(l)
print(arr)
n = int(input(print("Enter the number to be searched: ")))
result = binary_search(arr, n)
if result != -1:
    print("Element is present at ", result + 1)
else:
    print("Element is not present in array: ")