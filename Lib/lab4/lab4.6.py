def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r) / 100

    print('The Simple Interest is', si)
    return si


p1 = int(input("Enter P: "))
t1 = int(input("Enter T: "))
simple_interest(p1, t1, 8)