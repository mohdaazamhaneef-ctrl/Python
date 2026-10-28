# Exercise 13: Find the smallest number in a list

data = [22, 55, 12, 89, 34, 67]

smallest = data[0]

for num in data:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)
