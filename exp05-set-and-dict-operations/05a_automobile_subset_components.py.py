#declaring a set of components of a car 
car={'Engine','Battery','Alteernator','Radiator','Steering','Break','Seat Belt'}

#declaring a set of components of motorbike
motorbike={'Engine','Fuel tank','Wheels','Gear','Break'}

#Elements of the set car
print('components of car:',car)

#Elements of the set motorbike
print('components of motorbike:',motorbike)

#union operation 
print('union of car and motorbike:',car|motorbike)

#intersection operation
print('intersection of car and motorbike:',car&motorbike)

#difference opetation 
print('Difference operation:',car-motorbike)

#Symmetric Difference
print('Symmetric difference operation:',car^motorbike)
