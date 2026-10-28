#Exercise1
students={"Rahul":75,"Amit":32,"Priya":88,"Neha":39,"Rohit":55}
for name, marks in students.items():
    if marks >= 40:
        print(name, "Passed")
    else:
        print(name,"Failed")

#Exercise2
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
    
#Exercise3
products={"Laptop":10,"Mouse":3,"Keyboard":0,"Monitor":7,"Printer":2}
for product, stock in products.items():
    if stock==0:
        print(product,"Out of stock")
    else:
        if stock<=5:
            print(product,"Low Stock")
        else:
            print(product,"Available")

#Exercise4
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


#Exercise4
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


#Exercise5
data={"a":10,"b":15,"c":25,"d":30,"e":40}
for key, value in data.items():
    if value%2==0 and value >20:
        print(key,"Large Even")
    elif value%2==0:
        print (key,"Even")
    else:
        print(key,"Odd")

#Exercise6
products={"Mobile":15000,"Mouse":500,"Laptop":60000,"Keyboard":1200}
for Product,price in products.items():
    if price>=1000:
        if price>=5000:
            print(Product,"Premium Product")
        else:
            print(Product,"Expensive Product")
    else:
        print(Product,"Affordable Product")


#Exercise7
students = {"Rahul":{"attendance":85,"marks":70},
            "Amit":{"attendance":60,"marks":80},
            "Priya":{"attendance":90,"marks":35},
            "Neha":{"attendance":78,"marks":55}}
for name, info in students.items():
    attendance=info["attendance"]
    marks=info["marks"]
    if attendance>=75:
        if marks>=40:
            print(name,"Eligible")
        else:
            print(name,"Failed in Exam")
    else:
        print(name,"Not Eligible")

#Exercise8 Bank Account Classification
accounts={"Rahul":25000,"Amit":5000,"Priya":0,"Neha":-2000}
for name,balance in accounts.items():
    if balance>0:
        if balance>=10000:
            print(name,"Premimum Account")
        else:
            print(name,"Regular Account")
    elif balance==0:
            print(name,"No Balance")
    else:
        print(name,"Overdraft")


#Experience10
students={"Rahul":{"marks":85,"attendance":90},
          "Amit":{"marks":35,"attendance":80},
          "Priya":{"marks":65,"attendance":70},
          "Neha":{"marks":45,"attendance":85},
          "Rohit":{"marks":90,"attendance":60}
          }
for name,info in students.items():
    marks=info["marks"]
    attendance=info["attendance"]
    if attendance>=75:
        if marks>=80:
           print(name,"Distrinction")
        elif marks>=60:
                print(name,"Frist Devision")
        elif marks>=40:
                print(name, "Pass")
        else:
                print(name, "Fail")
    else:
        print(name,"Not Eligible")


#Exercise9
employees = {
    "Rahul": {"salary": 60000, "experience": 5},
    "Amit": {"salary": 45000, "experience": 2},
    "Priya": {"salary": 75000, "experience": 7},
    "Neha": {"salary": 35000, "experience": 1},
    "Rohit": {"salary": 55000, "experience": 4}
}
for name, info in employees.items():
    salary=info["salary"]
    experience=info["experience"]
    if salary>=50000:
        if experience>=5:
            print(name,"Senior")
        else:
            print(name,"Mid Level")
    elif experience>=3:
        print(name,"Experienced Junior")
    else:
        print(name,"Fresher")
