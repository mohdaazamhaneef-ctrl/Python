# Exercise 15: Count the number of spaces in a sentence

text = "Python is easy to learn"

spaces = 0

for char in text:
    if char == " ":
        spaces += 1

print("Number of spaces:", spaces)
