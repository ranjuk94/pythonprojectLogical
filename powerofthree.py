n=int(input("enter a number:"))
flag=0
if n>0:
    for i in range(1,n):
        if pow(3,i)==n:
           flag=1

if flag:
    print("true")
else:
    print("false")