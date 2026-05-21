#Finding area of shapes 
def circle():
  r=float(input("Enter r value:"))
  return 3.14*r*r

def square():
  a=float(input("Enter a value:"))
  return a*a

def rectangle():
  l=float(input("Enter l value:"))
  b=float(input("Enter b value:"))
  return l*b

def triangle():
  b=float(input("Enter b value:"))
  h=float(input("Enter h value:"))
  return 0.5*h*b

print("select shape to calculate area:")

print("1.Circle")
print("2.Square")
print("3.Rectangle")
print("4.Triangle")
choice=int(input("enter choice(1/2/3/4): "))

if choice==1:
  print("Area of circle is %.2f"%circle())

elif choice==2:
  print("Area of square is %.2f"%square())

elif choice==3:
  print("Area of rectangle is %.2f"%rectangle())

elif choice==4:
  print("Area of triangle is %.2f"%triangle())

else:
  print("invalid output")
