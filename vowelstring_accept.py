x={'a','e','i','o','u'}
#x1={'A','E','I','O','U'}
y=input("Enter a string:")
y_lower=y.lower()
#print(y_lower)
y_lower_set=set(y_lower)
result_set=x&y_lower_set
# #print(y_set)
# #result_set=x&y_set
# #print(result_set)
if result_set==x:#result_set==x or result_set_y==x1:
      print("string accepted")
else:
      print("string is not accepted")

