def convertTuple(tup):

    str = ''
    for item in tup:
        str = str + item
    return str


tuple = ('g', 'a', 'u', 'r', 'a', 'v')
str = convertTuple(tuple)
print(str)