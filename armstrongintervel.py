start =int(input("enter start of the intervel:"))
stop = int(input("enter the end of the intervel:"))
for num in range(start,stop):
    length = len(str(num))
    temp=num
    sum=0
    while temp>0:
      digit = temp % 10
      sum+=digit**length
      temp//=10
    if num==sum:
        print(sum)

