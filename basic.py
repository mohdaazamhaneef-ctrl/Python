# A variable is a name given to a memory location in a program.
name = "Aazam"
age = 23
price = 25.99

print("my name is : ", name)
print("my age is : ", age)
print("price is : ", price)

# data type
name = "Aazam"
age = 23
price = 25.99

print(type(name))
print(type(age))
print(type(price))

# Arithmetic operators
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) # **mean square

# Relational/Comparison Operator (True/False)
a = 50
b = 20

print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False

# Assignment operator
num = 10
num += 10 # num=10+10
num -= 10 # num=10-10
num *= 10 # num=10*10
num /= 10 # num=10/10
num %= 10 # num=10%10
num **= 10 # num=10square

print("num :", num)

# Logical operator (not,and,or)
a = 50
b = 30
print(not False)
print(not a > b) # Oposite

val1 = True
val2 = True
print("and operator :" , val1 and val2) # if one val diff= False

print("OR operator :", (a ==b) or (a > b))