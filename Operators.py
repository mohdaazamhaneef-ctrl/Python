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