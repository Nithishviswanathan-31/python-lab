tax=0.18
Rate={"Pencil":10,"Pen":20,"Scale":7,"A4Sheet":150}
print("Retail Bill Calculator\n")
print("Enter the quantity of the ordered items:\n")
Pencil=int(input("Pencil:"))
Pen=int(input("Pen:"))
Scale=int(input("Scale:"))
A4Sheet=int(input("A4Sheet:"))
cost=Pencil*Rate["Pencil"]+Pen*Rate["Pen"]+Scale*Rate["Scale"]+A4Sheet*Rate["A4Sheet"]
Bill=cost+cost*tax
print("Please pay Rs.%f"%Bill)