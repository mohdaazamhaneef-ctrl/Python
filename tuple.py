# Tuple
    # Imp Point: Parentheses () are commonly useed to create tuple
    # But Parentheses are not actually mandatory
data = (10,20,30,40,50)
print(type(data))

# The comma , is what makes a tuple, not parentheses
data2 = 10,
print(type(data)) 

# Tuple indexing
data = (10,20,30,40,50)
print(data[2])
print(data[-1]) # Negative indexing starts from -1 from the right side.

# A tuple allowed duplicate elements
data = (10,20,30,40,50,30)
print(data)

# Tuple is immutable
# A Tuple is immutable, which means its elements cannot be changed, update or deleted after creation.
data = (10,20,30,40,50)
#data[0]=80              #TypeError: 'tuple' object does not support item assignment

# Tuple Packing
# Ex- 1
studentData = "Aazam", "MCA", 78.65
print(type(studentData)) 

# Ex- 2
record = "Aazam", "MCA", 23, True
print(record[0])
print([record[1]])
print(record)

# Ex- 3
record = "Aazam", "MCA", 23, True
name,*ab,att = record
print(name)
print(ab)
print(att)

# Tuple Unpacking
data = "Aazam", "MCA", 23, True
n,*ab = data
print(n)
print(ab)