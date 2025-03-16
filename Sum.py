sum=int(0)
checker=True
while checker==True:
    x=int(input("Enter a number:"))
    if x>=0:
        sum=sum+x
    else:
        checker=False

print ("The sum of the positive numbers is :",sum)
  