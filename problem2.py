#! python

a = input("Enter a number: ").strip()
a = int(a)
b = 0
c = 1
for i in range(0,a):
    b = a - i
    c = b * c

print(str(a)+"! is "+str(c) +" where "+str(a)+" is the integer entered and " +str(c)+ " is the calculated answer")