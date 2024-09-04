x=int(input("Enter the sum:"))
n=[1,2,3,4,5,6,7,8]
sum=0
length=len(n)
for i in range(0,length):
    for j in range(i+1,length):
        if n[i]+n[j] == x:
            sum = sum+1
            #result=n.append(i)

print(sum)