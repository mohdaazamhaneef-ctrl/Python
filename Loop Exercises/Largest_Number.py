# Exercise 12: Find the largest number in a list using a for loop

data = [22, 55, 12, 89, 34, 67]

largest = data[0]

for num in data:
    if num > largest:
        largest = num

print("Largest number:", largest)
