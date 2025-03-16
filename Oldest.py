x=int(input("enter the first age:"))
y=int(input("Enter the seecond age:"))
z=int(input("Enter the third age:"))
if x>y and x>z :
    print ("the Oldest:",x)
    if y>z:
        print("the Youngest:",z)
    else :
         print("the Youngest:",y)
elif y>x and y>z:
    print ("the Oldest:",y)
    if x>z:
        print("the Youngest:",z)
    else :
         print("the Youngest:",x)
elif z>x and z>y:
    print ("the Oldest:",z)
    if x>y:
        print("the Youngest:",y)
    else :
         print("the Youngest:",x)


