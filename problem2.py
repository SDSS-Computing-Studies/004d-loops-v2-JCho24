#! python

a = input("Enter a number: ").strip()
a = int(a)
t = a
h = a + 1
for i in range(1,h):
    a = a - 1
    b = t * a 
    c = b * a
    print(c)