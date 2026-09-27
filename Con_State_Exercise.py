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



experience=int(input("Enter employee experience year:"))
salary=int(input("enter salary:"))
performance=int(input("inter performance:"))
if(experience>=2):
    if(salary>=50000):
        if(performance>=90):
            bonus=salary*20/100
            print("Eligible for bonus");
            print("Bonus rate : 20%",bonus)
        elif(performance>=70):
            bonus=salary*10/100
            print("Eligible for bonus");
            print("Bonus rate : 10%",bonus)
        elif(performance<50000):
            print("eligible for bonus")
            print("Bonus rate : 15%")
        else:
            bonus=salary*5/100
            print("Bonus rate : 5%",bonus)
    else:
        print("Salary is too low")
else:
    print("experience is not eligible")
