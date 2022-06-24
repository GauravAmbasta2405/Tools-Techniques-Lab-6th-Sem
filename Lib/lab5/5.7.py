def Reverse(tuples):
    new_tup = ()

    for k in reversed(tuples):
        new_tup = new_tup + (k,)

    print(new_tup)

tuples = (10, 11, 12, 13, 14, 15)
Reverse(tuples)
