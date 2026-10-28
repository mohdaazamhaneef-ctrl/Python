#Employee Experience 
#Classify employees based on salary and experience. 
#Conditions: - Salary >= ₹50,000: 
  #- Experience >= 5 years -> Senior 
  #- Otherwise -> Mid-Level - Salary < ₹50,000: 
  #- Experience >= 3 years -> Experienced Junior 
  #- Otherwise -> Fresher/Junior
employees = {
    "Rahul": {"salary": 60000, "experience": 6},
    "Amit": {"salary": 45000, "experience": 4},
    "Priya": {"salary": 70000, "experience": 3},
    "Neha": {"salary": 30000, "experience": 1}
}

for name, details in employees.items():
    salary = details["salary"]
    experience = details["experience"]

    if salary >= 50000:
        if experience >= 5:
            category = "Senior"
        else:
            category = "Mid-Level"
    else:
        if experience >= 3:
            category = "Experienced Junior"
        else:
            category = "Fresher/Junior"

    print(name, category)