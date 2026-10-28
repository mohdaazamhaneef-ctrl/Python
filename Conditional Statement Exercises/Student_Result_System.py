# Exercise 2: Student Result System
#Write a program that takes marks of 3 subjects. 
#Conditions: 
#- If every subject has marks >= 40, calculate the percentage. 
#- If percentage >= 75, print "Distinction". 
#- If percentage >= 60, print "First Division". 
#- If percentage >= 50, print "Second Division". 
#- Otherwise, print "Pass". 
#- If any subject is below 40, print "Fail". 

sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))

if sub1 < 40 or sub2 < 40 or sub3 < 40:
    print("Result: Fail")
else:
    total = sub1 + sub2 + sub3
    percentage = total / 3

    print("Total Marks:", total)
    print("Percentage:", percentage, "%")

    if percentage >= 75:
        print("Result: Distinction")
    elif percentage >= 60:
        print("Result: First Division")
    elif percentage >= 50:
        print("Result: Second Division")
    else:
        print("Result: Pass")
