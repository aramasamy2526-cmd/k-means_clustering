#Mini Calculate
a = int(input("enter any number for a: "))
b = int(input("enter any number for b: "))
x = int(input("Enter 1 to do addition\nEnter 2 to do subtraction\nEnter 3 to do multiplication\nEnter 4 to do division: "))

if x==1:
    c = a+b
    print("addition of ",a,"and",b,"is",c)
elif x==2:
    c = a-b
    print("substration of ",a,"and",b,"is",c)
elif x==3:
    c = a*b
    print("Multiplication of ",a,"and",b,"is",c)
elif x==4:
    c = a/b
    print("division of ",a,"and",b,"is",c)
else:
    print("please type from 1 to 4 number only to do add, sub, multiplication and division")
