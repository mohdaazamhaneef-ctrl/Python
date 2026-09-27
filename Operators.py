#len() Returns total number of elements
data=(10,20,30,40,50,30)
print(len(data))

#count(): count how many time a value occurs
print(data.count(30))

print(sum(data))
print(max(data))
print(min(data))
print(data.index(10))

#Arithmatic Operators
x,y=10,20
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#floor devision
print(7/2)      #floor devision returns the floor value (greatest integer less than or equal to the result) 
print(-7/2)
print(2**3)     #Exponentiation **is used to calculate the power of number.

#Compound Assignment Operators
x,y=40,50
x+=y                #x=x+y
print(x)

x-=y
print(x)

x*=y
print(x)

x/=y
print(x)

#Relational / Comparision Operators
# The result of every relational operator is always a boolean value: True or False
x=10
y=20

print(x==y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x!=y)

#AND
#   FC      SC      Result
#   T       T       True
#   T       F       False
#   F       T       False

#OR
#   T       T       True
#   T       F       True
#   F       T       True
#   F       F       False


#Logical And Operators in python
x=10
y=20
print(x<y and y>x)
print(x<y and x==y)
print(x>y and x<y)
print(x>y and x==y)

#is operator: the is operator checks whether two variables refer to the same object in momery.
x=[10,20]
y=x
print(x is y)

print(id(x))   # id(): Merory identity of object
print(id(y))
print(x==y)

#== vs is with list
x=[10,20]
y=[10,20]

print(x==y)
print(x is y)
x.append(33)   # The list reffered by x is modified.
print(x==y)
print(id(x))
print(id(y))

#Membership Operators
# IN
data=[10,20,30,66,88]
print(22 in data)
print(20 in data)

#NOT IN
data=[10,20,30,66,88]
print(22 not in data)
print(20 not in data)

# Important for python, Pyhton does not support:
# i++ Post-increment
# ++i Pre-increment
# i-- Post-decrement
# --i Pre-decrement