#Progr to checking palindrome in string

s1=input("Enter a string")
s2=s1[::-1]
if list(s1)==list(s2):
  print("It is palindrome")
else:
  print("It is not a palindrome")
