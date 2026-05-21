#program for print number pattern 

print("Number pattern Printing")
rows=int(input("Enter no.of rows to print"))

for i in range(1,rows+1):
  for j in range(1,i+1):
    print(j),
  print("")