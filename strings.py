# escape sequence character
str = "This is a string.\nwe are creating it in python." #\n for new line, \t for tab space
print(str)

# concatenation (jodna)
str1 = "Mohd"
str2 = "Aazam"
print(str1 + str2)

# length of string
# example 1
str = "Mohd"
print(len(str))

# example 2
str1 = "Mohd"
str2 = "Aazam"
final_str = str1 + " " + str2
print(final_str)

# slicing
str = "Mohd Aazam"
print(str[1:4])
print(len(str[5:len(str)])) # len(str)=10
print(str[:4])
print(str[5:])

# negative indexing
str = "Aazam"
print(str[-5:-2])

#Strings Functions

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

#starstwith()
email="admin@gmail.com"
print(email.startswith("admin"))

#endswith()
email="admin@gmail.com"
print(email.endswith("com"))
print('@' in email)

#split()
data="I Love Python Programming"
newData=data.split()
print(data)
print(newData)

#join()
data=['I','Love','Python','Programming']
newData=" ".join(data)
print(newData)

#isalpha()
data="Invertis"         #data="Invertis123"   #False
print(data.isalpha())

#isdigit()
data="12345"            #data="Invertis123"   #False
print(data.isdigit())

#isalnum()
data="Invertis12345"    #data="Invertis@12345"   #False
print(data.isalnum())
