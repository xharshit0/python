a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the three number"))
d = int(input("Enter the four number"))

if (a >= b)and(a >= c) and (a >= d):
    print("a is greater than b , c and d")
elif(b >= a)and(b >= c) and (b >= d):
    print("b is greater than a ,c and d")
elif(c >= a)and(c >= b) and (c >= d):
    print("c is greater than a ,b and d")

else:
    print("d is greater than a , b and c")