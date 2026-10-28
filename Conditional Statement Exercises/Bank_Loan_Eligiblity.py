# Bank Loan Eligibility
#A bank gives a loan based on the following conditions: 
#- Age must be >= 21. 
#- If age is valid, salary must be >= ₹25,000. 
#- If salary is valid: 
#- Credit score >= 750: Loan approved. 
#- Credit score >= 650: Loan approved with higher interest. 
#- Otherwise: Loan rejected. 
age=int(input("Enter Age: "))
salary=int(input("Enter Salary: "))
credit_score=int(input("Enter Credit Score: "))
if (age>=21):
    if (salary>=25000):
        if (credit_score>=750):
            print("Loan Approved")
        elif (credit_score>=650):
            print("Loan Approved with higher interest")
        else:
            print("Loan Rejected")
    else:
        print("Salary is too low")
else:
    print("Age is not eligible")