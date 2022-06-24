str = input("Enter the string: ")
n = len(str)
arr = []
for i in range(0, n):
    for j in range(i, n):
        arr.append(str[i:(j+1)])

print("All subsets of the iven string: ")
for i in arr:
    print(i)