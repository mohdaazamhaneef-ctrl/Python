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
