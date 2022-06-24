string = input("Please enter a string: ")

string1 =' '

i=len(string)-1

while(i>=0):
    string1 = string1+string[i]
    i = i-1

print("\nReversed String: ", string1)