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