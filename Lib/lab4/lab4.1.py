def avg_num(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    return avg


num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

average = avg_num(num1, num2, num3)

print('The average of  three numbers = %0.2f' % average)