num =int(input("enter a number:"))
sum = 0
temp = num
while temp > 0:
    r = temp % 10
    sum+=r**3
    temp//=10
if num == sum:
    print("armstrong number")
else:
    print("not armstrong")
