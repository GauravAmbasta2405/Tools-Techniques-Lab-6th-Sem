from statistics import stdev
def sum_avg_standard(n1, n2, n3, n4, n5):
    sum_all = (n1+n2+n3+n4+n5)
    avg = sum_all/5
    arr = (n1, n2, n3, n4, n5)

    print('\nSum of all the numbers = %0.2f' % sum_all)
    print('\nAverage of all the numbers = %0.2f' % avg)
    print("Standard Deviation = %s" % (stdev(arr)))

num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))
num3 = float(input('Enter 3rd number: '))
num4 = float(input('Enter 4th number: '))
num5 = float(input('Enter 5th number: '))

sum_avg_standard(num1, num2, num3, num4, num5)


