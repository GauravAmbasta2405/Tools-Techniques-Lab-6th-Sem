s = "India stands for Unity"
l = []
temp =""
for i in range(0, len(s)):
    if s[i] == ' ':
        l.append(temp)
        temp = " "
    else:
        temp+=s[i]
for i in range(0, len(l), 2):
    print(l[i], end="")
    i+=1