p,q = None, None
#p & q here denotes rwo positive numbers

p= int(input("Enter number: "))
q= int(input("Enter number: "))
while p!=q:
        if p>q:
              p-=q
        else:
              q-=p
print("GCD of two number: ", p)