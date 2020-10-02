#! python

p = input("Enter a name: ").strip()

nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")
for i in nameList:
        if i == p:
         print("That name is on the list")
         break
else:
 print("That name is not on the list")