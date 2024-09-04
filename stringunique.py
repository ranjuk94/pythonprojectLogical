x="python"
flag = False
y = []
for i in x:
    if i not in y:
        y.append(i)
    else:
        flag = True
        break

if flag:
    print("the string is not unique")
else:
    print("the string is unique")
