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

# Q7: Print the multiplication table of 7. 
for i in range(1,11):
    print(7,"x",i,"=",7*i)

# Q8: Take a number from the user and print its multiplication table. 
num=int(input("Enter Number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

# Q9: Print numbers from 1 to 100 that are divisible by both 3 and 5. 
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)

#Q10: Count even and odd numbers between 1 and 50. 
count_even=0
count_odd=0
for i in range(1,51):
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("Even Numbers Count:",count_even)
print("Odd Numbers Count:",count_odd)

# Q11: Print the elements of a list in reverse order.
data = [22, 33, 12, 32, 45, 13]
data.reverse()
print(data)

# Q12: Find the largest number in a list using a for loop.
data = [22, 55, 12, 89, 34, 67]
largest=max(data)
print("Largest Number:",largest)

# Q13: Find the smallest number in a list.
data = [22, 55, 12, 89, 34, 67]
smallest=min(data)
print("Smallest Number:",smallest)

