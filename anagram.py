x=input("Enter first string:")
x1=x.upper()
y=input("Enter second string:")
y1=y.upper()
flag=0
if len(x1)==len(y1):
    for i in x1:
        if i in y1:
            flag=1
        else:
            flag=0
            break
if flag==1:
    print("anagram")
else:print("not anagram")

