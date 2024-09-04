x=int(input("enter a number:"))
temp=x
rem=0
sum=0
length=len(str(x))
#print(length)
while temp>0:
    rem=temp%10
    y=rem**length
    sum=sum+y
    temp=int(temp/10)
    length=length-1
#print(sum)
if sum==x:
    print("the number is disarium ")
else:
    print("the number is not disarium")
