x=[1,2,3,4,5,1,3,2]
length=len(x)
for i in range(0,length):
    for j in range(i+1,length):

        if x[i]==x[j]:
            print(x[j])
