x=[1,2,6,3,4,3,1,1]
length=len(x)
y=[]
for i in range(0,length):
    for j in range(i+1,length):

        if x[i]==x[j]:
            y.append(x[j])
#print(y)
z=set(x)-set(y)
print(list(z))


