#Employee Salary and Department
#The following dictionary contains employee salary and department. Display the employee category.
#Conditions:
#Salary >=50,000:
# IT - Senior IT Employee 
# HR->> Senior HR Employee 
# Other department
#Salary<50,000 - Junior Employee

employees={"Rahul":{"salary":60000,"department":"IT"},"Amit":{"salary":40000,"department":"HR"},"Priya":{"salary":70000,"department":"IT"},"Neha":{"salary":45000,"department":"Finance"}}
for name, info in employees.items():
    salary=info["salary"]
    department=info["department"]
    if salary>=50000:
        if department=="IT":
            print(name,"Senior IT Employee")
        elif department=="HR":
            print(name,"Seniro HR Employee")
        else:
            print(name,"Senior Employee")
    else:
        print(name,"junior Employee")