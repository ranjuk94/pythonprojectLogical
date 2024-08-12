x = int(input("Enter 3 Numbers:"))
y = int(input())
z = int(input())
if x > y and x > z:
      print("The largest number is:", x)

elif y > x and y > z:
    print("The largest number is:", y)
else:
    print("The largest number is:", z)