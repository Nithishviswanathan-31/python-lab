#program for calculating electricity bill in Python

units=int(input("Please enter the number of units you consumed in a month : "))

if(units<=100):
 payAmount=units*1.5
elif(units<=200):
 payAmount=(100*1.5)+(units-100)*2.5
elif(units<=300):
 payAmount=(100*1.5)+(200-100)*2.5+(units-200)*4
elif(units<=350):
 payAmount=(100*1.5)+(200-100)*2.5+(300-200)*4+(units-300)*5
else:
 payAmount=1500
Total=payAmount;
print("\nElectricity bill=%.2f" %Total)