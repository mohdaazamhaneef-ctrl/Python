data="Python"
print(data[0])      #indexing
print(data[0:6])    #slicing
print(data[-1])     #negative indexing
print(data*3)       
print(*[data]*3) 

#len()
data="Python Programming"
print(len(data))

#upper()
data="python Programming"
print(data.upper())

#lower()
data="Pyhton Programming"
print(data.lower())

#strip()
data="    Python Programming  "
print(data)
print(data.strip())

#lstrip()
data="    Python Programming  "
print(data)
print(data.lstrip())

#rstrip()
data="    Python Programming  "
print(data)
print(data.rstrip())

#replace()
data="Python Programming"
newData=data.replace("Python","Java")
print(data)
print(newData)

#find()
data="Python Programming"
print(data.find('P'))
print(data.find('Programming'))
print(data.find('z'))       

#index
data="Python Programming"
print(data.index('P'))
#print(data.index('z'))     ValueError: substring not found

#count()
data="Python Programming"
print(data.count('P'))
print(data.count('p'))