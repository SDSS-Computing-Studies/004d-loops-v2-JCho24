#! python

a = input("Enter an integer: ").strip()
a = int(a)
for i in range(1,13):
    i = a * i
    print(i)