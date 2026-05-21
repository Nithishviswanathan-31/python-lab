#program for exchanging two variable values

def exchange(x,y):
  x,y=y,x
  print("After exchange x,y")
  print("X=",x)
  print("Y=",y)
x=input("Enter value of X")
y=input("Enter value of Y")
print("Before exchange of x,y")
print("X=",x)
print("Y=",y)
exchange(x,y)