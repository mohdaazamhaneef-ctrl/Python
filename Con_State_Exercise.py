# Bank Loan Eligibility
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

#E-Commerce Discount
amount=int(input("Enter Amount: "))
Premium_Member=True
if (amount>=5000):
    if(Premium_Member):
        discount=amount*20/100
        print("Discount amount is: ",discount)
    else:
        discount=amount*10/100
        print("Discount amount is: ",discount)
elif(Premium_Member):
    discount=amount*5/100
    print("Discount amount is: ",discount)
else:
    discount=0
    print("Discount amount is: ",discount)

final_amount=amount-discount
print("Your final amount is: ",final_amount)



