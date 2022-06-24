from itertools import islice
Input = [1, 2, 3, 4, 5, 6, 7]

length_to_split = [2, 2, 3]
Input1 = iter(Input)

Output = [list(islice(Input1, elem))

          for elem in length_to_split]

print("Initial list is:", Input)

print("Split length list: ", length_to_split)

print("List after splitting: ", Output)