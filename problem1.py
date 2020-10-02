#! python

w = input("Enter a width: ").strip()
w = int(w)
h = input("Enter a height: ").strip()
h = int(h)
for i in range(h):
    for e in range(w):
        print("*", end="")
    print()

