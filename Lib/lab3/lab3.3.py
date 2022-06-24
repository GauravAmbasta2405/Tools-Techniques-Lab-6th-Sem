def reverse(str1):
    if (len(str1) == 0):
        return str1
    else:
        return reverse(str1[1:]) + str1[0]

string = input("Enter the String : ")
str1 = reverse(string)
if (string == str1):
    print("This is a Palindrome String")
else:
    print("This is Not a Palindrome String")