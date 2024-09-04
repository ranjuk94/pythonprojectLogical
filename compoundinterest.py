principal=float(input("enter the principal amount:"))
rate=float(input("Enter the interest rate:"))
time=int(input("enter the time period(in years):"))
#n=int(input("enter the no.of time interest applied:"))
amount=principal*(1+rate/time)**(time)
interest=0
interest = amount-principal
print(interest)
