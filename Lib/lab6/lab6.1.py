def unique_list(l):
    temp=[]
    for x in l:
        if x not in temp:
            temp.append(x)
    return temp


