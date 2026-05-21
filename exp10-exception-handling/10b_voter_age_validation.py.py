#program for finding greatest aming three numbers 
A=int(input("Enter the value of A:"))
B=int(input("Enter the value of B:"))
C=int(input("Enter the value of C:"))
if (A>B) and (A>C):
  largest=A
elif (B>A) and (B>C):
  largest=B
else:
  largest=C
print("The largest is",largest)