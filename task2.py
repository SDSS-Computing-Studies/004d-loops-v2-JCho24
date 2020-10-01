#! python

p = input("Enter a name: ")

people = ("Angela", "Dawson", "Max", "Daquavis")
for i in people:
    if p == i:
        print("It's a match")
        break
