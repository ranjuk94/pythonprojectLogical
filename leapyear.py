y = int(input("Enter an year:"))
if y % 4 == 0 and y%100 != 0:
    print("The year is Leap Year")
elif y % 100 == 0 or y%400 == 0:
   print("The year is Leap Year")
else:
    print("this year is not a leap year")