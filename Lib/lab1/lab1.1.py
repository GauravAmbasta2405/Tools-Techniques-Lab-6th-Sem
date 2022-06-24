string=input("Enter a string: \n")
global length
def find_length(string):
    length=0
    for i in string:
        length+=1
    return length
print(find_length(string))