num=int(input("enter a number:"))
sum=0
while num>0:
    digit=num%10
    sum=int(sum+digit)
    num=num/10
print(sum)
