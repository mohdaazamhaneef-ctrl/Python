# Exercise 6: Find the sum of odd numbers from 1 to 100
total = 0
for num in range(1, 101):
    if num % 2 != 0:
        total += num
print("Sum of odd numbers:", total)
