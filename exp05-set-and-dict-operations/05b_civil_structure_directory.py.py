#declare a dictionary building 
building={1:'foundation',2:'floor',3:'beams',4:'columns',5:'roof',6:'stair'}

#Elements in dictionary 
print('Elements in dictonary building:',building)

#length of a dictionary 
print('Length of the dictionary building:',len(building))

#value of the key 5
print('The value of the key 5',building.get(5))

#update key 6:stairs as lift
building.update({6:'lift'})
print('After updation of stairs as lift:',building)

#Add element window in dictionary
building[7]='window'
print('After addng window:',building)

#using pop operation to remove element
building.pop(3)
print('After removing elements beam from building:',building)
