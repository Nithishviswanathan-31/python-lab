file =open("F:\Data.txt","rt")
data=file.read()
words=data.split()
print('Number of words in textfile:',len(words))