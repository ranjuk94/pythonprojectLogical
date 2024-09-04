x=[3,4]
length1=len(x)
sum=0
if length1 == 2:
    print(max(x))

else:
      for i in range(0, length1):
        x1 = x[::2]
        length2 = len(x1)
      for i in range(0, length2):
        sum = sum + x1[i]

print("total amount:",sum)