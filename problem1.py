#! python

w = input("Enter a width: ")
w = int(w)
h = input("Enter a height: ")
h = int(h)
for i in range(h):
    for e in range(w):
        print("*", end="")
    print()

