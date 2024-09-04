for i in range(1,101):

    temp=str(i)
    sum=0

    for j in range(len(temp)):
         x=int(temp[j])
         #y=x**(i+1)
         sum=sum+x**(j+1)
         if sum==i:
             print(sum)
