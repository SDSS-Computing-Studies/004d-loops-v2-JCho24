#! python

a = int(input("int number that is smaller than 10: "))

b = 1

print("The sum of the series is ", end="")
for i in range(0,a):
    print(b, end="")
    
    b = b + 1