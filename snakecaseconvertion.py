x=input("Enter a snake case string:")
#x='hello_world'
x1=x.split('_')
y=[]
for i in x1:
    i=i.title()
    y.append(i)
y="".join(y)
print(str(y))
#x_split_pascal=x_split.title()
