#if statement
age=int(input("Enter User Age: "))
if (age>=18):
    print("Valid for voting")

#if else statement
age=int(input("Enter User Age: "))
if (age>=18):
    print("Valid for voting")
else:
    print("Not valid for voting")

# To check Even or odd number
num=int(input("Enter Number"))
if (num%2==0):
    print("Number is Even")
else:
    print("Number is Odd")

# To check Number is Positive Or Negative
num=int(input("Enter Number"))
if (num>0):
    print("Number is Positive")
else:
    print("Number is Negative")

#if elif else statement
marks=int(input("Enter Marks: "))
if (marks>=90):
    print("Grade A")
elif (marks>=80):
    print("Grade B")
elif (marks>=70):
    print("Grade C")
elif (marks>=60):
    print("GradeD")
else:
    print("Failed")


#idpass
age=int(input("Enter Age: "))
idPass=False
if (age>=18):
    if (idPass==True):
        print("Student Entry Allowed")
    else:
        print("Student have no ID. Entry not Allowed")
else:
    print("Student age is not valid. Entry not Allowed")