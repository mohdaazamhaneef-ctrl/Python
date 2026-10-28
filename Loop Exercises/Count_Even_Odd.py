# Exercise 10: Count even and odd numbers between 1 and 50
even_count = 0
odd_count = 0
for num in range(1, 51):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
