#! python

a = input("int number that is smaller than 10: ").strip()
a = int(a)
b = 1

print("the sum of the series is ", end="")
for i in range(1,a + 1):
    print(b, end="")
    
    b = b + 1