x=[1,2,2,3,3,3,4]
length=len(x)
frequency=0
y=int(input("enter the element to find the frequency:"))
for i in range(0,length):
    if x[i]==y:
        frequency=frequency+1
#frequency = x.count(y)

print(frequency)