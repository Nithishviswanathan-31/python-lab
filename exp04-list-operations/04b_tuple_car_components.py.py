#declearing a tuple of Components of a car 
car=('Engine','Battery','Alternator','Radiator','Steering','Break','Seat Belt')

#printing the complete tuple 
print('Components of a car:',car)

#printing first element
print('first element:',car[0])

#printing fourth element 
print('fourth element:',car[3])

#printing tuple elements from oth index to 4th index 
print('Componrnts of a car from o to 4 th index:',car[0:5])

#finding index of a specified element 
print('index of\'Alternator\':',car.index('Alternator'))

#Number of elements in car tuple
print('Number of Seat Belt in car tuple:',car.count('Seat Belt'))

#length of car tuple
print('Length of car Elements in car Tuple:',len(car))
