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
data[0]=80              #TypeError: 'tuple' object does not support item assignment