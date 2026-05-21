#Finding largest number in list 

def maximum(list):
  return max(list)
  
list=[]
n=int(input("Entet no.of.elements"))
print("Enter","num","elements")
i=0
for i in range(0,n):
  element=int(input())
  list.append(element)
print("Largest element is:",maximum(list))
