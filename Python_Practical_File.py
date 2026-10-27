# Q1: Print all even numbers from 1 to 20. 
for i in range(1,21):
    if i%2==0:
        print(i)

# Q2: Print all odd numbers from 1 to 20. 
for i in range(1,20):
    if i%2!=0:
        print(i)

# Q3: Print multiples of 5 from 5 to 50. 
for i in range(5,51,5):
    print(i)

# Q4: Find the sum of numbers from 1 to 10. 
total=0
for i in range(1,11):
    total+=i
print("Sum=",total)

# Q5: Find the sum of even numbers from 1 to 100. 
total=0
for i in range(1,101):
    if i%2==0:
        total+=i
print("sum of even numbers=",total)

# Q6: Find the sum of odd numbers from 1 to 100. 
total=0
for i in range(1,101):
    if i%2!=0:
        total+=i
print("sum of odd numbers=",total)