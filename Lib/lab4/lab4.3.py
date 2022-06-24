def LCMHCF(a, b):
    HCF = 1

    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            HCF = i

    print("HCF of two numbers is: ", HCF)

    LCM = int((a * b) / HCF)
    print("LCM of two numbers is: ", LCM)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
LCMHCF(a, b)