students={"Rahul":75,"Amit":32,"Priya":88,"Neha":39,"Rohit":55}
for name, marks in students.items():
    if marks >= 40:
        print(name, "Passed")
    else:
        print(name,"Failed")

students={"Rahul":75,"Amit":32,"Priya":88,"Neha":39,"Rohit":55}
marks=0
if marks>=80:
    print("Exellent")
elif marks>=60:
    print("Good")
elif marks>=40:
    print("Average")
else:
    print("Failed")
    
products={"Laptop":10,"Mouse":3,"Keyboard":0,"Monitor":7,"Printer":2}
for product, stock in products.items():
    if stock==0:
        print(product,"Out of stock")
    else:
        if stock<=5:
            print(product,"Low Stock")
        else:
            print(product,"Available")

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


employees={"Rahul":{"salary":60000,"Experience":6},"Amit":{"salary":40000,"Experience":3},"Priya":{"salary":70000,"Experience":8},"Neha":{"salary":45000,"Experience":4}}
for name, info in employees.items():
    Salary=info["salary"]
    Experience=info["Experience"]
    if Salary>=50000:
        if Experience>=5:
            print(name,"Senior")
        elif Experience>=3:
                print(name,"Experienced Junior")
        else:
            print(name,"Fresher/Junior")
    else:
        print(name,"Mid Level")