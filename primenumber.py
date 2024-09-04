x = int(input("Enter a number:"))
flag=0
if x==0 or x==1:
    print("The number is not prime")
if x>1:
 for i in range(2,x):
    if (x % i) == 0:
        flag = 1
        break
if flag == 1:
    print("not prime")
else:
    print("prime")