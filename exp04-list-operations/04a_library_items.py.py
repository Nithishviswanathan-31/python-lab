#declaring a list of items in a library 

library=['Books','Periodicals','Newspaper','Manscripts','Maps','Prints','Documents','Ebooks']

#printing the complete list 
print('Library:',library)

#printing first element
print('first element:',library[0])

#print fourth element 
print('fourth element:',library[3])

#print list elements from 0th index to 4th index
print('Items in library from 0 to 4 index:',library[0:5])

#appending an element to the list 
library.append('Audiobooks')
print('Library list after append Audiobooks:',library)

#finding index of a specified element
print('index of\'Newspaper\':',library.index('Newspaper'))

#sorting the elements of list
library.sort()
print('after sorting:',library);

#popping an element
print('Popped elements is:',library.pop())
print('after pop():',library);

#removing specified element 
library.remove('Maps')
print('after removing \'Maps\':',library)

#inserting an element at specified index #inserting CD at 2nd index 
library.insert(2,'CDs')
print('after insert CDs:',library)

#Number of Elements in Library list
print('Number of Elements in Library list :',len(library))