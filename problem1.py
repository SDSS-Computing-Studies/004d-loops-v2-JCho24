#! python

w = input("Enter a width: ").strip()
w = int(w)

for i in range(1,w + 1):
    print("*" * w)

